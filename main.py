# -*- coding = utf-8 -*-
# 开发时间：2022/5/10 20:05
import pygame
import random
import sys
from pygame.locals import *

caption_width = 500
caption_height = 500  # 设置窗口大小
white_color = (255, 255, 255)  # 设置白色的参数
blcak_color = (0, 0, 0)
game_title = '贪吃蛇'  # 设置游戏名称
cell = 10
snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]  # 蛇的初始位置
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]  # 食物初始随机位置
head_pos = [250, 250]  # 蛇头的位置

pygame.init()  # pygame的初始化,窗口通过pygame的初始化就可以使用它提供给的工具

caption = pygame.display.set_mode((caption_width, caption_height))   # 窗口
pygame.display.set_caption(game_title)      # 标题


def draw_rect(color, position):         # 将画图抽成一个方法
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))


def change_direction(head_pos):         # 将移动和加格抽成一个方法
    global food_pos
    snake_init_pos.insert(0, list(head_pos))
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1,50) * 10, random.randrange(1, 50) * 10]


def hit_the_self():
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True
    else:
        return False


def hit_the_wall(head_pos):
    if head_pos[0] >= caption_width or head_pos[0] < 0 or head_pos[1] >= caption_height or head_pos[1] < 0:
        return True
    else:
        return False


clock = pygame.time.Clock()


def main():
    pygame.mixer.music.load("bgmusic.ogg")
    pygame.mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('左')
                    head_pos[0] -= cell
                    change_direction(head_pos)
                    print(snake_init_pos)
                elif event.key == pygame.K_RIGHT:
                    print('右')
                    head_pos[0] += cell
                    change_direction(head_pos)
                    print(snake_init_pos)
                elif event.key == pygame.K_UP:
                    print('上')
                    head_pos[1] -= cell
                    change_direction(head_pos)
                    print(snake_init_pos)
                elif event.key == pygame.K_DOWN:
                    print('下')
                    head_pos[1] += cell
                    change_direction(head_pos)
                    print(snake_init_pos)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if hit_the_self() or hit_the_wall(head_pos):
                pygame.quit()
        clock.tick(30)
        caption.fill(blcak_color)
        for pos in snake_init_pos:
            draw_rect(white_color, pos)
        draw_rect(white_color, food_pos)
        pygame.display.update()


main()
