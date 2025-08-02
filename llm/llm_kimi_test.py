"""
Minimal character-level Transformer on Shakespeare.
~5 min on CPU, ~30 s on GPU.
"""
import os, math, random, requests, torch
from torch import nn

# ---------- 1. 下载数据 ----------
DATA_URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
if not os.path.exists("shakespeare.txt"):
    open("shakespeare.txt", "w", encoding="utf-8").write(requests.get(DATA_URL).text)
text = open("shakespeare.txt", encoding="utf-8").read()
print(f"Corpus length: {len(text):,} characters")

# ---------- 2. 字符级分词 ----------
chars = sorted(list(set(text)))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: "".join(itos[i] for i in l)
vocab_size = len(stoi)

# ---------- 3. 超参 ----------
block_size = 128      # 上下文长度
batch_size = 64
d_model = 256
nhead = 8
num_layers = 6
dropout = 0.1
device = "cuda" if torch.cuda.is_available() else "cpu"
steps = 5000
lr = 3e-4

# ---------- 4. 数据加载 ----------
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data, val_data = data[:n], data[n:]

def get_batch(split):
    d = train_data if split == "train" else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    x = torch.stack([d[i:i+block_size] for i in ix])
    y = torch.stack([d[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

# ---------- 5. 模型 ----------
class TransformerModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb   = nn.Embedding(block_size, d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, dropout=dropout, batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, idx, targets=None):
        b, t = idx.size()
        pos = torch.arange(0, t, dtype=torch.long, device=device).unsqueeze(0)
        tok_emb = self.token_emb(idx) + self.pos_emb(pos)
        mask = nn.Transformer.generate_square_subsequent_mask(t).to(device)
        x = self.transformer(tok_emb, mask)
        logits = self.head(self.ln_f(x))

        loss = None
        if targets is not None:
            loss = nn.functional.cross_entropy(
                logits.view(-1, vocab_size), targets.view(-1), ignore_index=-1
            )
        return logits, loss

model = TransformerModel().to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

# ---------- 6. 训练 ----------
for step in range(1, steps+1):
    xb, yb = get_batch("train")
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    if step % 200 == 0 or step == 1:
        print(f"step {step:5d} | loss {loss.item():.4f}")

# ---------- 7. 生成 ----------
context = torch.zeros((1, 1), dtype=torch.long, device=device)  # 从换行符开始
gen_len = 500
model.eval()
with torch.no_grad():
    for _ in range(gen_len):
        logits, _ = model(context[:, -block_size:])
        logits = logits[:, -1, :]
        probs = torch.softmax(logits, dim=-1)
        next_id = torch.multinomial(probs, num_samples=1)
        context = torch.cat((context, next_id), dim=1)
print("="*80)
print(decode(context[0].tolist()))