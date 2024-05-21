import torch
from torch import nn


################
# 网络部分
################

# 对抗性正则化器,设定了图片是256*256
class ICCN(nn.Module):
    # 仿照对抗性正则化器中卷积识别器的设定
    def __init__(self, ndc, nc, img_size, a=1e-3):
        super(ICCN, self).__init__()

        # 第一层的权重不用任何处理，因此独立出来，将后面的模块作为一个整体进行处理
        self.preprocessing = nn.Sequential()
        self.preprocessing.add_module("Conv, channels:{0}-{1}, conv".format(nc, ndc),
                                      nn.Conv2d(nc, ndc, 4, 2, 1))  # 第一层是卷积层
        self.preprocessing.add_module("LeakyReLU", nn.LeakyReLU(0.02, inplace=True))

        # 创建需要权重裁剪的两个模块
        self.main = nn.Sequential()
        img_size //= 2

        while img_size > 16:
            img_size //= 2  # 每次经过conv后，图片大小变为原大小的1/2
            ndc *= 2
            self.main.add_module("Conv, channels:{0}-{1}".format(ndc // 2, ndc),
                                 nn.Conv2d(ndc // 2, ndc, 4, 2, 1))
            self.main.add_module(f"LeakyReLU{img_size}", nn.LeakyReLU(0.02, inplace=True))

        self.main.add_module(f"Conv,{ndc}-{2 * ndc}",
                             nn.Conv2d(ndc, 2 * ndc, 4, 2, 1))
        self.main.add_module(f"ReLU, {ndc}-{2 * ndc}",
                             nn.ReLU(inplace=True))

        # 输出时，特征图的大小应该是(8, 8)， channels应该是现在的ndc
        self.postprocessing = nn.Sequential(
            nn.Conv2d(2 * ndc, 1, 1, 1, 0),
        )

        self.ndc = ndc
        self.img_size = img_size
        self.a = a

    # 初始化各个层的权重
    def initialize(self):
        # 对self.preprocessing进行正常初始化
        for module in self.preprocessing.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.002)
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

        # 对self.main和self.postprocessing进行初始化并裁剪非负
        for module in self.main.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.002)
                module.weight.data.clamp_(min=0)  # 裁剪非负
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

        for module in self.postprocessing.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.002)
                module.weight.data.clamp_(min=0)  # 裁剪非负
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

    # 该方法需要在每次优化后进行调用，以保证神经网络的凸性结构
    def convex_constraint(self):
        # 只需要对main和postprocessing进行处理
        for layer in self.main:
            if hasattr(layer, 'weight'):
                layer.weight.data.clamp_(min=0)

        for layer in self.postprocessing:
            if hasattr(layer, 'weight'):
                layer.weight.data.clamp_(min=0)
            if hasattr(layer, 'bias'):
                layer.bias.data.clamp_(min=0)

    def forward(self, x):
        output0 = self.preprocessing(x)
        output1 = self.main(output0)
        output2 = self.postprocessing(output1)

        img_l2_square = torch.norm(x, p=2, dim=(1, 2, 3)) ** 2
        NN_l2_square = torch.norm(output2, p=2, dim=(1, 2, 3)) ** 2

        return (self.a * img_l2_square + NN_l2_square)


# 对于通道数为1的图片构建的全局平均池化激活的神经网络
class ICCN_layer_Avg(nn.Module):
    # 仿照对抗性正则化器中卷积识别器的设定
    def __init__(self, ndc, nc, img_size):
        super(ICCN_layer_Avg, self).__init__()

        # 第一层的权重不用任何处理，因此独立出来，将后面的模块作为一个整体进行处理
        self.preprocessing = nn.Sequential()
        self.preprocessing.add_module("Conv, channels:{0}-{1}, conv".format(nc, ndc),
                                      nn.Conv2d(nc, ndc, 4, 2, 1))  # 第一层是卷积层
        self.preprocessing.add_module(f"Layernorm, img_size{img_size}",
                                      nn.LayerNorm(img_size // 2, eps=1e-5, elementwise_affine=True))
        self.preprocessing.add_module("LeakyReLU", nn.LeakyReLU(0.02, inplace=True))

        # 创建需要权重裁剪的两个模块
        self.main = nn.Sequential()
        img_size //= 2

        while img_size > 8:
            img_size //= 2  # 每次经过conv后，图片大小变为原大小的1/2
            ndc *= 2
            self.main.add_module("Conv, channels:{0}-{1}".format(ndc // 2, ndc),
                                 nn.Conv2d(ndc // 2, ndc, 4, 2, 1, bias=False))
            self.main.add_module(f"Layernorm, img_size{img_size}",
                                 nn.LayerNorm(img_size, eps=1e-5, elementwise_affine=True))
            self.main.add_module("LeakyReLU", nn.LeakyReLU(0.02, inplace=True))

        # 输出时，特征图的大小应该是(8, 8)， channels应该是现在的ndc

        self.postprocessing = nn.Sequential(
            nn.Conv2d(ndc, 1, 1, 1, 0),
        )

        self.ndc = ndc

    # 初始化各个层的权重
    def initialize(self):
        # 对self.preprocessing进行正常初始化
        for module in self.preprocessing.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.02)
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

        # 对self.main和self.postprocessing进行初始化并裁剪非负
        for module in self.main.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.02)
                module.weight.data.clamp_(min=0)  # 裁剪非负
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

        for module in self.postprocessing.modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                nn.init.normal_(module.weight.data, 0.0, 0.02)
                module.weight.data.clamp_(min=0)  # 裁剪非负
                if module.bias is not None:
                    nn.init.constant_(module.bias.data, 0)

    # 该方法需要在每次优化后进行调用，以保证神经网络的凸性结构
    def convex_constraint(self):
        # 只需要对main和postprocessing进行处理
        for layer in self.main:
            if hasattr(layer, 'weight'):
                layer.weight.data.clamp_(min=0)

        for layer in self.postprocessing:
            if hasattr(layer, 'weight'):
                layer.weight.data.clamp_(min=0)

    def forward(self, x):
        output0 = self.preprocessing(x)
        output1 = self.main(output0)
        output2 = self.postprocessing(output1)
        return output2


if __name__ == "__main__":
    img_size = 256
    batch_size = 64
    nc = 1
    ndc = 32

    imgs = torch.rand((64, 1, 256, 256))
    net = ICCN(ndc, nc, img_size)
    net.initialize()
    net.convex_constraint()
    print(net)