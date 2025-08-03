import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import numpy as np


# 位置编码：给模型提供序列位置信息
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()

        # 计算位置编码
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, 1, d_model)
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)

        self.register_buffer('pe', pe)  # 不参与训练的参数

    def forward(self, x):
        # x: (seq_len, batch_size, d_model)
        x = x + self.pe[:x.size(0)]
        return x


# 多头注意力机制，允许模型同时关注序列的不同部分
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0, "d_model必须能被num_heads整除"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # 每个头的维度

        # 线性变换层
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)

        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        batch_size = q.size(0)

        # 线性变换并分成多头
        q = self.w_q(q).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(k).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(v).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # 计算注意力分数
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        # 应用掩码（在解码时使用，防止关注未来的词）
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        # 计算注意力权重
        attn = F.softmax(scores, dim=-1)

        # 应用注意力到值
        output = torch.matmul(attn, v)

        # 拼接多头结果
        output = output.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # 输出线性变换
        return self.w_o(output), attn


# 前馈神经网络，处理注意力机制输出的特征
class FeedForward(nn.Module):
    def __init__(self, d_model, hidden_dim, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(d_model, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, d_model)
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.GELU()  # 使用GELU激活函数

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x


# Transformer 解码器层，包含自注意力和前馈网络
class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, hidden_dim, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = FeedForward(d_model, hidden_dim, dropout)

        # 层归一化
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        #  dropout层
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # 自注意力子层
        attn_output, attn_weights = self.self_attn(x, x, x, mask)
        x = x + self.dropout1(attn_output)
        x = self.norm1(x)

        # 前馈子层
        ff_output = self.feed_forward(x)
        x = x + self.dropout2(ff_output)
        x = self.norm2(x)

        return x, attn_weights


# 简化的Transformer语言模型，整的语言模型，使用多个解码器层堆叠
class SimpleTransformerLM(nn.Module):
    def __init__(self, vocab_size, d_model=128, num_heads=4,
                 num_layers=2, hidden_dim=256, dropout=0.1):
        super().__init__()
        self.d_model = d_model

        # 词嵌入层
        self.embedding = nn.Embedding(vocab_size, d_model)

        # 位置编码,为输入序列添加位置信息，让模型理解词语的顺序关系
        self.pos_encoder = PositionalEncoding(d_model)

        # 解码器层
        self.decoder_layers = nn.ModuleList([
            DecoderLayer(d_model, num_heads, hidden_dim, dropout)
            for _ in range(num_layers)
        ])

        # 输出层，预测下一个词
        self.fc_out = nn.Linear(d_model, vocab_size)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # x: (batch_size, seq_len)

        # 词嵌入 + 位置编码
        x = self.embedding(x) * math.sqrt(self.d_model)
        x = self.pos_encoder(x.transpose(0, 1)).transpose(0, 1)
        x = self.dropout(x)

        # 通过解码器层
        attn_weights = []
        for layer in self.decoder_layers:
            x, attn = layer(x, mask)
            attn_weights.append(attn)

        # 输出预测
        logits = self.fc_out(x)  # (batch_size, seq_len, vocab_size)

        return logits, attn_weights


# 生成因果掩码（防止模型看到未来的词）
def generate_causal_mask(seq_len):
    mask = (torch.triu(torch.ones(seq_len, seq_len)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf'))
    return mask


# 文本生成函数，基于已训练的模型生成新文本
def generate_text(model, tokenizer, start_text, max_length=50, temperature=0.7):
    model.eval()
    device = next(model.parameters()).device

    # 编码起始文本
    input_ids = tokenizer.encode(start_text).unsqueeze(0).to(device)

    for _ in range(max_length):
        # 获取当前序列长度
        seq_len = input_ids.shape[1]

        # 生成掩码
        mask = generate_causal_mask(seq_len).to(device)

        # 模型预测
        with torch.no_grad():
            logits, _ = model(input_ids, mask)

        # 取最后一个词的logits
        next_token_logits = logits[:, -1, :] / temperature

        # 应用softmax获取概率
        next_token_probs = F.softmax(next_token_logits, dim=-1)

        # 采样下一个词
        next_token_id = torch.multinomial(next_token_probs, num_samples=1).squeeze(1)

        # 添加到输入
        input_ids = torch.cat([input_ids, next_token_id.unsqueeze(0)], dim=-1)

        # 如果生成了结束标记，停止
        if next_token_id.item() == tokenizer.eos_token_id:
            break

    # 解码生成的文本
    generated_text = tokenizer.decode(input_ids.squeeze().tolist())
    return generated_text


# 简单的Tokenizer类，简单的分词器，将文本转换为模型可处理的数字 ID
class SimpleTokenizer:
    def __init__(self, text=None):
        self.word2idx = {'<pad>': 0, '<unk>': 1, '<sos>': 2, '<eos>': 3}
        self.idx2word = {v: k for k, v in self.word2idx.items()}
        self.vocab_size = 4

        if text:
            self.build_vocab(text)

    def build_vocab(self, text):
        # 简单分词（按空格）
        words = text.split()
        for word in words:
            if word not in self.word2idx:
                self.word2idx[word] = self.vocab_size
                self.idx2word[self.vocab_size] = word
                self.vocab_size += 1

    def encode(self, text):
        words = text.split()
        # 添加开始标记
        encoded = [self.word2idx['<sos>']]
        for word in words:
            encoded.append(self.word2idx.get(word, self.word2idx['<unk>']))
        # 添加结束标记
        encoded.append(self.word2idx['<eos>'])
        return torch.tensor(encoded, dtype=torch.long)

    def decode(self, ids):
        words = []
        for idx in ids:
            if idx == self.word2idx['<eos>']:
                break
            words.append(self.idx2word.get(idx, '<unk>'))
        return ' '.join(words)

    @property
    def pad_token_id(self):
        return self.word2idx['<pad>']

    @property
    def eos_token_id(self):
        return self.word2idx['<eos>']


# 模型训练函数，实现了基本的训练循环
def train_model(model, tokenizer, train_data, epochs=10, batch_size=4, lr=1e-3):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # 准备数据加载器
    dataset = torch.utils.data.TensorDataset(train_data)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # 损失函数和优化器
    criterion = nn.CrossEntropyLoss(ignore_index=tokenizer.pad_token_id)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(epochs):
        total_loss = 0

        for batch in dataloader:
            optimizer.zero_grad()

            # 获取输入和目标（目标是输入右移一位）
            x = batch[0].to(device)
            y = x[:, 1:].contiguous()  # 目标是输入右移一位
            x_input = x[:, :-1].contiguous()  # 输入是目标左移一位

            # 生成掩码
            seq_len = x_input.size(1)
            mask = generate_causal_mask(seq_len).to(device)

            # 前向传播
            logits, _ = model(x_input, mask)

            # 计算损失
            loss = criterion(logits.transpose(1, 2), y)
            total_loss += loss.item()

            # 反向传播和优化
            loss.backward()
            optimizer.step()

        avg_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.4f}')

        # 每个epoch结束后生成一些文本作为示例
        if (epoch + 1) % 2 == 0:
            sample_text = generate_text(model, tokenizer, "the", max_length=20)
            print(f"Sample generation: {sample_text}\n")

    return model


# 示例用法
if __name__ == "__main__":
    # 准备训练数据（这里使用简单的文本作为示例）
    sample_text = """
    the quick brown fox jumps over the lazy dog .
    never jump over the lazy dog quickly .
    quick brown foxes leap over lazy dogs in summer .
    the quick brown fox jumped over the lazy dog .
    a quick movement of the enemy will jeopardize six gunboats .
    """

    # 创建分词器并构建词汇表
    tokenizer = SimpleTokenizer(sample_text)
    print(f"Vocabulary size: {tokenizer.vocab_size}")

    # 准备训练数据
    sentences = [s.strip() for s in sample_text.split('.') if s.strip()]
    max_len = max(len(sentence.split()) + 2 for sentence in sentences)  # +2 for sos and eos

    # 对句子进行编码和填充
    encoded_sentences = []
    for sentence in sentences:
        encoded = tokenizer.encode(sentence)
        # 填充到最大长度
        if len(encoded) < max_len:
            pad_length = max_len - len(encoded)
            encoded = torch.cat([encoded, torch.full((pad_length,), tokenizer.pad_token_id, dtype=torch.long)])
        encoded_sentences.append(encoded)

    train_data = torch.stack(encoded_sentences)

    # 创建模型
    model = SimpleTransformerLM(
        vocab_size=tokenizer.vocab_size,
        d_model=64,
        num_heads=2,
        num_layers=2,
        hidden_dim=128
    )

    # 训练模型
    print("开始训练模型...")
    trained_model = train_model(model, tokenizer, train_data, epochs=20, batch_size=2)

    # 生成文本示例
    print("生成文本示例:")
    print(generate_text(trained_model, tokenizer, "quick", max_length=30))
    print(generate_text(trained_model, tokenizer, "the fox", max_length=30))
    print(generate_text(trained_model, tokenizer, "lazy", max_length=30))
