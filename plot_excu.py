import numpy as np
import os
from plot_main import plot_eps, save_image  # 根据你的模块名称或结构调整导入语句

# 定义参数以加载和显示线图
line_data_path = r"C:\Users\13621\Desktop\结果传输\data52934\iNETT_iter_test32_v2_0.1\npy\64Loss.npy"  # 线图数据文件路径
line_x_label = "k"
line_y_label = "AR loss"
line_directory = r"C:\Users\13621\Desktop\bachelor_thesis\figures\iNETT"
line_name = "arloss"

# 定义参数以加载和显示图像
image_data_path = "./data/noise_image_data.npy"  # 随机噪声图像数据文件路径
image_cmap = 'hot'  # 图像的颜色映射
image_directory = "./data"
image_name = "noise_image"
image_channels = 1  # 灰度图像

if __name__ == "__main__":
    # 从文件加载数据
    line_data = np.load(line_data_path)
    # image_data = np.load(image_data_path)

    # 显示并保存线图
    plot_eps(line_data, line_x_label, line_y_label, show=True, save=True, directory=line_directory, name=line_name, log=True)

    # 保存图像
    # save_image(image_data, channels=image_channels, cmap=image_cmap, show=False, save=True, directory=image_directory, name=image_name, eps=True)
