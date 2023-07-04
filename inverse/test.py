import torch
import torch.nn as nn
import time
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

if_cuda = torch.cuda.is_available()
print("if_cuda=", if_cuda)

gpu_count = torch.cuda.device_count()
print("gpu_count=", gpu_count)

# 2，将张量在gpu和cpu间移动
tensor = torch.rand((100, 100))
tensor_gpu = tensor.to("cuda:0")  # 或者 tensor_gpu = tensor.cuda()
print(tensor_gpu.device)
print(tensor_gpu.is_cuda)

tensor_cpu = tensor_gpu.to("cpu")  # 或者 tensor_cpu = tensor_gpu.cpu()
print(tensor_cpu.device)

net = nn.Linear(2, 1)
print(next(net.parameters()).is_cuda)
net.to("cuda:0")  # 将模型中的全部参数张量依次到GPU上，注意，无需重新赋值为 net = net.to("cuda:0")
print(next(net.parameters()).is_cuda)
print(next(net.parameters()).device)

# 准备数据
n = 1000000  # 样本数量

X = 10 * torch.rand([n, 2]) - 5.0  # torch.rand是均匀分布
w0 = torch.tensor([[2.0, -3.0]])
b0 = torch.tensor([[10.0]])
Y = X @ w0.t() + b0 + torch.normal(0.0, 2.0, size=[n, 1])  # @表示矩阵乘法,增加正态扰动

# 移动到GPU上
print("torch.cuda.is_available() = ", torch.cuda.is_available())
X = X.cuda()
Y = Y.cuda()
print("X.device:", X.device)
print("Y.device:", Y.device)


# 定义模型
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.randn_like(w0))
        self.b = nn.Parameter(torch.zeros_like(b0))

    # 正向传播
    def forward(self, x):
        return x @ self.w.t() + self.b


linear = LinearRegression()

# 移动模型到GPU上
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
linear.to(device)

# 查看模型是否已经移动到GPU上
print("if on cuda:", next(linear.parameters()).is_cuda)

# 训练模型
optimizer = torch.optim.Adam(linear.parameters(), lr=0.1)
loss_func = nn.MSELoss()


def train(epoches):
    tic = time.time()
    for epoch in range(epoches):
        optimizer.zero_grad()
        Y_pred = linear(X)
        loss = loss_func(Y_pred, Y)
        loss.backward()
        optimizer.step()
        if epoch % 50 == 0:
            print({"epoch": epoch, "loss": loss.item()})
    toc = time.time()
    print("time used:", toc - tic)


train(500)
