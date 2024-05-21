# import pickle
import os
import numpy as np
from matplotlib import pyplot as plt
from networks import *

# 模型的路径与保存模型的
model_path = "data/netC_CT500.path"
file_dir = r'C:\Users\13621\Desktop\结果传输\data52934\param_save'
# 创建
os.makedirs(file_dir, exist_ok=True)
# file_path = f"{file_dir}/model_params.pkl"

# 先创建一个模型实例
nc = 1
img_size = 256
ndc = 32
gpu_ids = [0]

net = ICCN(ndc, nc, img_size)
net = torch.nn.DataParallel(net, gpu_ids)

# 加载训练的模型
model = torch.load(model_path)
net.load_state_dict(model)

# 保存训练结果的文件夹
save_dir = file_dir

# 打印模型训练后的数据
model_params = {}
for name, param in net.named_parameters():
    print(name)
    name=name.split('.')[1] + name.split(':')[1]
    param = param.data.view(-1).cpu().numpy()
    model_params[name] = param  # 转换为numpy数组方便查看和兼容性
    indices = np.arange(len(param))
    np.save(save_dir + f'/{name}.npy', param)
    print('save already')

    # plt.plot(indices, param, label=name)
    # plt.legend()
    # # plt.title(name)
    # plt.xlabel("Index")
    # plt.ylabel("Values")
    # plt.savefig(f"{save_dir}/{name}.eps", format='eps')
    # plt.close()
    # print(f"{save_dir}/{name}.eps" + "Saved!")

"""# 以下操作用于保存模型训练后的数据，通过以下两个步骤保存和加载数据以供查看
with open('model_params.pkl', 'wb') as f:
    pickle.dump(model_params, f)

with open('model_params.pkl', "rb") as f:
    params_dict = pickle.load(f)"""