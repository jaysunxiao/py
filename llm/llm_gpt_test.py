import torch
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import random

# 准备字符级语料数据
text = "hello world! this is a simple gpt model. let's see how it performs. "

# 创建字符字典
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

def encode(s): return [stoi[c] for c in s]
def decode(l): return ''.join([itos[i] for i in l])

# 超参数
block_size = 16
batch_size = 8
n_embd = 32
n_layer = 2
n_head = 4
learning_rate = 1e-3
max_iters = 300

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 构造训练样本
data = torch.tensor(encode(text), dtype=torch.long)

def get_batch():
    ix = torch.randint(len(data) - block_size - 1, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

# 简易 GPT 模型
class TinyGPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(block_size, n_embd)
        self.blocks = nn.ModuleList([
            nn.TransformerEncoderLayer(d_model=n_embd, nhead=n_head)
            for _ in range(n_layer)
        ])
        self.ln_f = nn.LayerNorm(n_embd)
        self.head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx):
        B, T = idx.shape
        tok = self.token_emb(idx)
        pos = self.pos_emb(torch.arange(T, device=idx.device))
        x = tok + pos
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        logits = self.head(x)
        return logits

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits = self(idx_cond)
            probs = F.softmax(logits[:, -1, :], dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, next_token), dim=1)
        return idx

model = TinyGPT().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# 训练主循环
for iter in tqdm(range(max_iters)):
    xb, yb = get_batch()
    logits = model(xb)
    loss = F.cross_entropy(logits.view(-1, vocab_size), yb.view(-1))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if iter % 50 == 0:
        print(f"Step {iter}: loss {loss.item():.4f}")

# 生成文本
context = torch.tensor([[stoi['h']]], dtype=torch.long).to(device)
generated = model.generate(context, max_new_tokens=100)[0].tolist()
print("\nGenerated:\n" + decode(generated))
