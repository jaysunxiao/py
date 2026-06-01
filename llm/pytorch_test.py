import torch

print(
    "--------------------------------------------------------------------------------------"
)
print(torch.__version__)  # 输出版本号，如 2.0.1
print(torch.cuda.is_available())  # 检查 GPU 是否可用（True/False）

print(
    "--------------------------------------------------------------------------------------"
)
# 1. 创建 Tensor
tensor0d = torch.tensor(1)  # 零维张量（标量）
tensor1d = torch.tensor([1, 2, 3])  # 一维张量（向量）
tensor2d = torch.tensor(
    [
        [1, 2, 3],  # 维张量
        [4, 5, 6],
    ]
)

tensor3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 三维张量
print("tensor1d dtype:[{}]".format(tensor1d.dtype))  # Python 默认的 64 位整数数据类型
print("tensor2d shape:[{}]".format(tensor2d.shape))  # .shape 属性允许我们访问张量的形状

floatvec = torch.tensor([1.0, 2.0, 3.0])
print(
    "floatvec dtype:[{}]".format(floatvec.dtype)
)  # 果使用 Python 浮点数创建张量，那么 PyTorch 默认会创建具有 32 位精度的张量

tensor1d2floatvec = tensor1d.to(torch.float32)  # 可以使用张量的.to 方法更改精度
print("tensor1d2floatvec to float32 dtype:[{}]".format(tensor1d2floatvec.dtype))

print(tensor2d.view(3, 2))  # 要将该张量变为 3×2 的形状，可以使用 .view 方法
print(tensor3d.T)
print(
    "--------------------------------------------------------------------------------------"
)
# 4. 张量运算（类似 NumPy）
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
print(x + y)  # 加法
print(x * y)  # 元素乘法
print(torch.matmul(x, y))  # 矩阵乘法（等价于 x @ y）

input_ids = torch.tensor([2, 3, 5, 1])  # 要加入2,3,5,1的字符
vocab_size = 6  # 嵌入层需要支持的唯一标记的总数
output_dim = 3  # 嵌入向量的维度

torch.manual_seed(123)  # 用于设置随机数生成器的种子，确保结果的可复现性
embedding_layer = torch.nn.Embedding(
    vocab_size, output_dim
)  # 每行表示一个标记的嵌入向量。
print(embedding_layer.weight)
print(embedding_layer(torch.tensor([3])))
print(input_ids)
print(embedding_layer(input_ids))
