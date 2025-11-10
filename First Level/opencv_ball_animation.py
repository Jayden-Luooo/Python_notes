import numpy as np
import cv2
import time

# 创建黑色画布
height, width = 480, 640
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# 小球起始参数
x, y = 100, 100
vx, vy = 3, 2  # 速度

while True:
    # 清空画布
    canvas[:] = 0

    # 更新小球位置
    x += vx
    y += vy

    # 碰到边界反弹
    if x <= 20 or x >= width - 20:
        vx = -vx
    if y <= 20 or y >= height - 20:
        vy = -vy

    # 画小球
    cv2.circle(canvas, (x, y), 20, (0, 255, 0), -1)

    # 显示动画帧
    cv2.imshow('Ball Animation', canvas)

    # 延时并监听退出
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
