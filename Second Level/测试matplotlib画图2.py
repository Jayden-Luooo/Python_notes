import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  # 用于设置坐标轴整数刻度

# 设置中文字体，确保所有中文正常显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
plt.rcParams["font.size"] = 10  # 全局字体大小
plt.rcParams["axes.titlepad"] = 15  # 标题与坐标轴的距离
plt.rcParams["axes.labelpad"] = 10  # 标签与坐标轴的距离

# --------------------------
# 替换这里的示例数据为你的原始数据
# --------------------------
# 站点序号（x轴）
station_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 各时段客流量数据（y轴）- 替换为你的真实数据
# 例如：早高峰出站、早高峰进站、平峰出站、平峰进站等
morning_out = [120, 150, 180, 220, 200, 190, 160, 140, 130, 110, 100, 90, 80, 70, 60]
morning_in = [90, 110, 130, 160, 180, 170, 150, 130, 120, 100, 90, 80, 70, 60, 50]
flat_out = [80, 90, 110, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55]
flat_in = [60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]

# --------------------------
# 创建图表并设置细节
# --------------------------
# 创建画布，设置合适的大小（宽12英寸，高8英寸）
plt.figure(figsize=(12, 8))

# 绘制折线，添加更多视觉细节
# 早高峰出站 - 红色实线，圆形标记
plt.plot(station_numbers, morning_out, 
         label="早高峰出站", 
         color="#e74c3c",  # 红色
         linestyle="-", 
         linewidth=2.5,
         marker="o",       # 圆形标记
         markersize=8,     # 标记大小
         markerfacecolor="#c0392b",  # 标记填充色
         markeredgewidth=1.5)        # 标记边缘宽度

# 早高峰进站 - 红色虚线，方形标记
plt.plot(station_numbers, morning_in, 
         label="早高峰进站", 
         color="#e74c3c", 
         linestyle="--", 
         linewidth=2,
         marker="s",       # 方形标记
         markersize=7,
         markerfacecolor="white",
         markeredgewidth=1.5)

# 平峰出站 - 蓝色实线，三角形标记
plt.plot(station_numbers, flat_out, 
         label="平峰出站", 
         color="#3498db",  # 蓝色
         linestyle="-", 
         linewidth=2.5,
         marker="^",       # 三角形标记
         markersize=8,
         markerfacecolor="#2980b9",
         markeredgewidth=1.5)

# 平峰进站 - 蓝色虚线，菱形标记
plt.plot(station_numbers, flat_in, 
         label="平峰进站", 
         color="#3498db", 
         linestyle="--", 
         linewidth=2,
         marker="D",       # 菱形标记
         markersize=7,
         markerfacecolor="white",
         markeredgewidth=1.5)

# --------------------------
# 添加图表细节元素
# --------------------------
# 设置标题和坐标轴标签，增加字体细节
plt.title("北京地铁各站点客流量变化趋势", 
          fontsize=16, 
          fontweight="bold", 
          pad=20)  # 标题与图表的距离

plt.xlabel("站点序号", 
           fontsize=14, 
           fontweight="medium")

plt.ylabel("客流量（人）", 
           fontsize=14, 
           fontweight="medium")

# 设置坐标轴范围，让数据更居中
plt.xlim(min(station_numbers) - 0.5, max(station_numbers) + 0.5)  # x轴范围
plt.ylim(0, max(morning_out + morning_in + flat_out + flat_in) * 1.1)  # y轴范围（留10%余量）

# 设置坐标轴刻度为整数（站点序号和人数都是整数）
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))  # x轴只显示整数
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # y轴只显示整数

# 添加网格线，让数据读取更方便
plt.grid(True, 
         linestyle=":",  # 虚线网格
         alpha=0.7)      # 透明度70%

# 优化图例位置和样式
plt.legend(loc="upper right",  # 图例位置
           fontsize=12,       # 图例字体大小
           frameon=True,      # 显示图例边框
           framealpha=0.9,    # 边框透明度
           edgecolor="gray")  # 边框颜色

# 添加注释文本（可选，标记特殊站点）
# 例如：标记客流量最高的站点
max_flow_station = station_numbers[morning_out.index(max(morning_out))]
max_flow_value = max(morning_out)
plt.annotate(f'早高峰最大客流\n站点 {max_flow_station}: {max_flow_value}人',
             xy=(max_flow_station, max_flow_value),
             xytext=(max_flow_station+1, max_flow_value+50),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

# 调整布局，避免元素重叠
plt.tight_layout()

# 显示图表
plt.show()