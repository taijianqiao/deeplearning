import torch
import torch.nn as nn
#定义全连接神经网络
class AFullNet(nn.Module):
    def __init__(self):
        super().__init__()
        #下面创建4个全连接网络层：
        self.fc1 = nn.Linear(4, 5)  # 如果不设置偏置项，则添加参数bias=False即可，下同
        self.fc2 = nn.Linear(5,6)  # 【此处为本例核心代码，已省略，完整代码见教材P62；建议读者手工输入核心代码并进行调试，这样方能领会其含义】
        self.fc3 = nn.Linear(6,4)
        self.fc4 = nn.Linear(4, 3)
    def forward(self, x):
        out = self.fc1(x)
        # out = torch.tanh(out)  # 【此处为本例核心代码，已省略，完整代码见教材P62；建议读者手工输入核心代码并进行调试，这样方能领会其含义】
        # out = self.fc2(out)
        # # out = torch.rule(out)
        # out = self.fc3(out)
        # # out = torch.sigmoid(out)
        # out = self.fc4(out)

        return out
anet = AFullNet()
sum = 0
for para in anet.parameters():  #计算整个网络的参数量
    # n = 1
    # for i in para.shape: #统计每层的参数量
    #     n = n*i
    # sum += n
    print(torch.numel(para))
    sum += torch.numel(para)
print('该网络参数总量：%d'%sum)
exit(0)