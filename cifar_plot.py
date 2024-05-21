import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_cifar10_image_grid(dataset_path, grid_size=(8, 8), save_to='./data', show=False, eps=True, png=True,
                            wspace=0.0001, hspace=0.0001, figsize=(8, 8), name='cifar10_image_grid'):
    # 加载CIFAR-10数据集
    dataset = torchvision.datasets.CIFAR10(root=dataset_path, train=True, download=True)

    # 获取图像和标签
    images, labels = zip(*[(np.array(img), label) for img, label in dataset])
    num_images = grid_size[0] * grid_size[1]

    # 创建画布
    fig, axes = plt.subplots(grid_size[0], grid_size[1], figsize=figsize)
    plt.subplots_adjust(wspace=wspace, hspace=hspace)

    for ax, img in zip(axes.flat, images[:num_images]):
        ax.imshow(img)
        ax.axis('off')

    print(f'Saved image dimensions: {plt.gcf().get_size_inches()} inches')
    plt.tight_layout()

    if eps:
        plt.savefig(os.path.join(save_to, name + '.eps'), format='eps')

    if png:
        plt.savefig(os.path.join(save_to, name + '.png'))

    if show:
        plt.show()

    plt.close()


# 调用函数示例
plot_cifar10_image_grid('datasets', save_to=r'C:\Users\13621\Desktop\bachelor_thesis\figures\WGAN', show=True, eps=True, png=False, name='cifimage', wspace=0, hspace=0)
