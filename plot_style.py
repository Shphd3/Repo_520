import matplotlib.pyplot as plt

def set_plot_style():
    # 设置字体
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Times New Roman', 'SimSun']  # 包括Times New Roman和宋体以支持中文显示
    plt.rcParams['axes.unicode_minus'] = False  # 用于正确显示负号

    # # 设置图表标题和轴标签的大小(font08)
    # plt.rcParams['axes.titlesize'] = 14  # 设置图表标题的字体大小
    # plt.rcParams['axes.labelsize'] = 17.6  # 设置轴标签的字体大小
    # plt.rcParams['xtick.labelsize'] = 10  # 设置x轴刻度标签的字体大小
    # plt.rcParams['ytick.labelsize'] = 10  # 设置y轴刻度标签的字体大小
    #
    # # 设置图像分辨率
    # plt.rcParams['savefig.dpi'] = 300

# # 设置图表标题和轴标签的大小(font04)
#     plt.rcParams['axes.titlesize'] = 14  # 设置图表标题的字体大小
#     plt.rcParams['axes.labelsize'] = 31  # 设置轴标签的字体大小
#     plt.rcParams['xtick.labelsize'] = 14  # 设置x轴刻度标签的字体大小
#     plt.rcParams['ytick.labelsize'] = 14  # 设置y轴刻度标签的字体大小
#
#     # 设置图像分辨率
#     plt.rcParams['savefig.dpi'] = 300

# 设置图表标题和轴标签的大小(font06)
    plt.rcParams['axes.titlesize'] = 14  # 设置图表标题的字体大小
    plt.rcParams['axes.labelsize'] = 23.46 # 设置轴标签的字体大小
    plt.rcParams['xtick.labelsize'] = 14  # 设置x轴刻度标签的字体大小
    plt.rcParams['ytick.labelsize'] = 14  # 设置y轴刻度标签的字体大小

    # 设置图像分辨率
    plt.rcParams['savefig.dpi'] = 300