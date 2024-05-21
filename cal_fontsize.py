def calculate_fontsize(target_width_ratio, textwidth_pt, original_img_width_in, desired_fontsize_pt):
    """
    计算在matplotlib中应设置的字体大小，以便在LaTeX文档中保持字体大小一致。

    参数:
    target_width_ratio (float): 目标图像宽度占textwidth的比例，如0.4代表0.4\textwidth。
    textwidth_pt (float): LaTeX中的\textwidth，以pt为单位。
    original_img_width_in (float): 图像的原始宽度，以英寸为单位。
    desired_fontsize_pt (float): LaTeX中期望的字体大小，以pt为单位。

    返回:
    float: 应在matplotlib中使用的字体大小（pt）。
    """
    # 将\textwidth从pt转换为英寸
    textwidth_in = textwidth_pt / 72.27  # 1 inch = 72.27 pt

    # 计算图像在LaTeX中的显示宽度（英寸）
    target_width_in = textwidth_in * target_width_ratio

    # 计算缩放比例
    scaling_factor = target_width_in / original_img_width_in

    # 计算matplotlib中的字体大小
    matplotlib_fontsize_pt = desired_fontsize_pt / scaling_factor

    return matplotlib_fontsize_pt

# 示例用法
target_width_ratio = 0.6  # 比如0.4\textwidth
textwidth_pt = 345        # LaTeX中的\textwidth大小
original_img_width_in = 6.4  # 图像原始宽度，英寸
desired_fontsize_pt = 10.5   # LaTeX中的期望字号，五号字

# 调用函数计算字号
matplotlib_fontsize = calculate_fontsize(target_width_ratio, textwidth_pt, original_img_width_in, desired_fontsize_pt)
print(f"The font size to be used in matplotlib is {matplotlib_fontsize:.2f} pt.")