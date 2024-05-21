import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib
import os
from plot_style import set_plot_style

def plot_tikz(array, x_label, y_label, show=False, save=True, directory='./data', name='plot', log=False):
    set_plot_style()
    x = np.arange(len(array))
    plt.figure()
    if log:
        plt.semilogy(x, array)
    else:
        plt.plot(x, array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title('Plot in TikZ format')
    plt.tight_layout()  # 确保元素不被裁剪
    if save:
        file_path = os.path.join(directory, name +'.tex')
        os.makedirs(directory, exist_ok=True)
        tikzplotlib.save(file_path)
        print(f"Saved TikZ figure at '{file_path}'")
    if show:
        plt.show()
    print(f'Saved figure dimensions: {plt.gcf().get_size_inches()} inches')
    plt.close()

def plot_eps(array, x_label, y_label, show=False, save=True, directory='./data', name='plot', log=False):
    set_plot_style()
    x = np.arange(len(array))
    plt.figure()
    if log:
        plt.semilogy(x, array)
    else:
        plt.plot(x, array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title('Plot in EPS format')
    plt.tight_layout()
    if save:
        file_path = os.path.join(directory, name + '.eps')
        os.makedirs(directory, exist_ok=True)
        plt.savefig(file_path, format='eps')
        print(f"Saved EPS figure at '{file_path}'")
    if show:
        plt.show()
    print(f'Saved figure dimensions: {plt.gcf().get_size_inches()} inches')
    plt.close()

def plot_png(array, x_label, y_label, show=False, save=True, directory='./data', name='plot', log=False):
    set_plot_style()
    x = np.arange(len(array))
    plt.figure()
    if log:
        plt.semilogy(x, array)
    else:
        plt.plot(x, array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title('Plot in PNG format')
    plt.tight_layout()
    if save:
        file_path = os.path.join(directory, name + '.png')
        os.makedirs(directory, exist_ok=True)
        plt.savefig(file_path, format='png')
        print(f"Saved PNG figure at '{file_path}'")
    if show:
        plt.show()
    print(f'Saved figure dimensions: {plt.gcf().get_size_inches()} inches')
    plt.close()

def save_image(array, channels=1, cmap='viridis', show=False, save=True, directory='./data', name='image', eps=True, png=False):
    set_plot_style()
    plt.figure()
    if channels == 1:
        img = plt.imshow(array, cmap=cmap)
    else:
        img = plt.imshow(array)
    plt.colorbar(img)
    # plt.title('Image with Colorbar')
    plt.tight_layout()
    if save:
        os.makedirs(directory, exist_ok=True)
        if eps:
            file_path = os.path.join(directory, name + '.eps', format='eps')
            plt.savefig(file_path)
        if png:
            file_path = os.path.join(directory, name + '.png', format='png')
            plt.savefig(file_path)
        print(f"Saved image with colorbar at '{file_path}'")
    if show:
        plt.show()
    print(f'Saved image dimensions: {plt.gcf().get_size_inches()} inches')
    plt.close()


if __name__ == '__main__':
    # 示例数组
    data = np.random.rand(10)

    # 使用示例
    plot_png(data, 'Index', 'Value', show=True)
    save_image(np.outer(np.arange(10), np.arange(10)), channels=1, show=True)
