import numpy as np
import matplotlib.pyplot as plt
import os


def plot_npy_image_grid(directory, grid_size=(8, 8), save_to='./data', show=False, eps=True, png=True,
                        wspace=0.0001, hspace=0.0001, figsize=(8, 8), name='npy_image_grid'):
    # 读取文件夹中的所有.npy文件
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.npy')]
    num_images = grid_size[0] * grid_size[1]

    # 仅读取所需数量的图片
    images = [np.load(f) for f in files[:num_images]]

    # 创建画布
    fig, axes = plt.subplots(grid_size[0], grid_size[1], figsize=figsize)
    plt.subplots_adjust(wspace=wspace, hspace=hspace)

    for ax, img in zip(axes.flat, images):
        ax.imshow(img)
        ax.axis('off')
    print(f'Saved image dimensions: {plt.gcf().get_size_inches()} inches')
    plt.tight_layout()

    if eps:
        plt.savefig(os.path.join(save_to, name + '.eps'), format='eps')

    if png:
        plt.savefig(os.path.join(save_to, name + '.png'))

    if show == True:
        plt.show()

    plt.close()


if __name__ == '__main__':
    # 调用函数
    plot_npy_image_grid(r'C:\Users\13621\Desktop\结果传输\data52934\np_cp', save_to=r'C:\Users\13621\Desktop\bachelor_thesis\figures\WGAN', eps=True, png=False, show=False, name='cp')
