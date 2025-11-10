import cv2
import numpy as np
import random
import math

# 配置参数
BALL_NUM = 8
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 25
TAIL_LENGTH = 25

# 随机生成小球初始参数
def random_color():
    return (random.randint(100,255), random.randint(100,255), random.randint(100,255))

class Ball:
    def __init__(self):
        self.x = random.randint(BALL_RADIUS, WIDTH-BALL_RADIUS)
        self.y = random.randint(BALL_RADIUS, HEIGHT-BALL_RADIUS)
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(3, 8)
        self.vx = math.cos(angle)*speed
        self.vy = math.sin(angle)*speed
        self.color = random_color()
        self.radius = BALL_RADIUS
        self.tail = []

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # 边界碰撞
        if self.x < self.radius:
            self.x = self.radius
            self.vx *= -1
        if self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius
            self.vx *= -1
        if self.y < self.radius:
            self.y = self.radius
            self.vy *= -1
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy *= -1
        # 更新拖尾
        self.tail.append((int(self.x), int(self.y)))
        if len(self.tail) > TAIL_LENGTH:
            self.tail.pop(0)
        # 动态变色
        hsv = cv2.cvtColor(np.uint8([[self.color]]), cv2.COLOR_BGR2HSV)
        hsv[0,0,0] = (hsv[0,0,0] + 3) % 180
        self.color = tuple(int(x) for x in cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)[0,0])

def balls_collide(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    dist = math.hypot(dx, dy)
    return dist < ball1.radius + ball2.radius

def resolve_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    nx, ny = dx / dist, dy / dist
    p = 2 * (ball1.vx*nx + ball1.vy*ny - ball2.vx*nx - ball2.vy*ny) / 2
    ball1.vx -= p * nx
    ball1.vy -= p * ny
    ball2.vx += p * nx
    ball2.vy += p * ny
    # 分开叠在一起的球
    overlap = (ball1.radius + ball2.radius - dist) / 2
    ball1.x += nx * overlap
    ball1.y += ny * overlap
    ball2.x -= nx * overlap
    ball2.y -= ny * overlap

def draw_glow(img, x, y, radius, color):
    overlay = img.copy()
    for i in range(1, 7):
        alpha = 0.08 * (1 - i/7)
        cv2.circle(overlay, (int(x), int(y)), int(radius*(1+i*0.8)), color, -1)
        img = cv2.addWeighted(overlay, alpha, img, 1-alpha, 0)
    return img

def draw_tail(img, tail, color):
    for i in range(1, len(tail)):
        alpha = i / len(tail)
        cv2.line(img, tail[i-1], tail[i],
                 (int(color[0]*alpha), int(color[1]*alpha), int(color[2]*alpha)),
                 thickness=8, lineType=cv2.LINE_AA)
    return img

def main():
    balls = [Ball() for _ in range(BALL_NUM)]
    bg = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    while True:
        frame = bg.copy()
        # 小球之间碰撞检测
        for i in range(len(balls)):
            for j in range(i+1, len(balls)):
                if balls_collide(balls[i], balls[j]):
                    resolve_collision(balls[i], balls[j])
        # 绘制所有小球
        for ball in balls:
            ball.move()
            frame = draw_glow(frame, ball.x, ball.y, ball.radius, ball.color)
            draw_tail(frame, ball.tail, ball.color)
            cv2.circle(frame, (int(ball.x), int(ball.y)), ball.radius, ball.color, -1, lineType=cv2.LINE_AA)
        # 粒子星空点缀
        for _ in range(20):
            px = random.randint(0, WIDTH-1)
            py = random.randint(0, HEIGHT-1)
            cv2.circle(frame, (px, py), 1, (255,255,255), -1)
        cv2.imshow('Colorful Ball Animation', frame)
        key = cv2.waitKey(16)
        if key == 27 or key == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()