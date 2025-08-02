import torch
print(torch.__version__)  # 输出版本号，如 2.0.1
print(torch.cuda.is_available())  # 检查 GPU 是否可用（True/False）

# 1. 创建 Tensor
a = torch.tensor([1, 2, 3])  # 从列表创建
b = torch.zeros(2, 3)  # 2行3列的全0张量
c = torch.ones(3, 3)   # 3行3列的全1张量
d = torch.randn(2, 2)  # 2行2列的随机张量（正态分布）

# 2. 查看属性
print(a.shape)  # 形状：torch.Size([3])
print(b.dtype)  # 数据类型：torch.float32
print(c.device)  # 设备：cpu（默认）

# 3. 转换设备（GPU/CPU）
if torch.cuda.is_available():
    a_gpu = a.to('cuda')  # 移到 GPU
    print(a_gpu.device)  # 输出：cuda:0

# 4. 张量运算（类似 NumPy）
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
print(x + y)  # 加法
print(x * y)  # 元素乘法
print(torch.matmul(x, y))  # 矩阵乘法（等价于 x @ y）