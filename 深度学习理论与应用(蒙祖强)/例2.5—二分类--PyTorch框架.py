import torch
import matplotlib.pyplot as plt
import torch.nn as nn

# 读入数据
X1 = [2.49, 0.50, 2.73, 3.47, 1.38, 1.03, 0.59, 2.25, 0.15, 2.73]
X2 = [2.86, 0.21, 2.91, 2.34, 0.37, 0.27, 1.73, 3.75, 1.45, 3.42]
Y = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]  # 类标记
X1 = torch.Tensor(X1)
X2 = torch.Tensor(X2)
X = torch.stack((X1, X2), dim=1)  # 将所有特征数据“组装”为一个张量
Y = torch.Tensor(Y)  # 形状为torch.Size([10])

# 定义类Perceptron2
class Perceptron2(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.Tensor([0.0]))
        self.w2 = nn.Parameter(torch.Tensor([0.0]))
        self.b = nn.Parameter(torch.Tensor([0.0]))

    def f(self, x):
        x1, x2 = x[0], x[1]
        t = self.w1 * x1 + self.w2 * x2 + self.b
        z = 1.0 / (1 + torch.exp(t))
        return z

    def forward(self, x):
        pre_y = self.f(x)
        return pre_y

# 创建实例perceptron2
perceptron2 = Perceptron2()
optimizer = torch.optim.Adam(perceptron2.parameters(), lr=0.1)

# 以下开始训练
for ep in range(100):
    for (x, y) in zip(X, Y):
        pre_y = perceptron2(x)
        y = torch.Tensor([y])
        loss = nn.BCELoss()(pre_y, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# 至此，训练完毕
s = '学习到的感知器：pre_y = sigmoid(%0.2f*x1 + %0.2f*x2 + %0.2f)' % (
    perceptron2.w1.item(), perceptron2.w2.item(), perceptron2.b.item())
print(s)

for (x, y) in zip(X, Y):
    t = 1 if perceptron2.f(x) > 0.5 else 0
    s = ''
    if t == y.item():
        s = '点(%0.2f, %0.2f)被<正确>分类！' % (x[0], x[1])
    else:
        s = '点(%0.2f, %0.2f)被<错误>分类！' % (x[0], x[1])
    print(s)

# ----- 以下为非必要代码，仅用于绘制散点图和学习到的直线 -----
# 绘制散点图
t1 = [i for (i, e) in enumerate(Y) if e == 0]
t2 = [i for (i, e) in enumerate(Y) if e == 1]
X1, X2 = X[t1], X[t2]
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c='r')
plt.scatter(X2[:, 0], X2[:, 1], marker='v', c='g')

# 绘制直线
def g(x1):
    x2 = -(perceptron2.w1 * x1 + perceptron2.b) / perceptron2.w2
    return x2

xmin, xmax = X[:, 0].min(), X[:, 0].max()
T1 = [xmin, xmax]
T2 = [g(xmin), g(xmax)]

# 将 T1 和 T2 转换为 numpy 数组
T1 = [t.detach().numpy() if isinstance(t, torch.Tensor) else t for t in T1]
T2 = [t.detach().numpy() if isinstance(t, torch.Tensor) else t for t in T2]

plt.plot(T1, T2, '--', c='b')
plt.grid()
plt.tick_params(labelsize=13)
plt.xlabel("x$_1$", fontsize=13)
plt.ylabel("x$_2$", fontsize=13)
plt.show()