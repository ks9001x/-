# -*- coding = utf-8 -*-
# 开发时间：2022/5/10 20:05
import pygame
import random
import time
import sys
from pygame.locals import *
# 导入tkinter库
from tkinter import *
import tkinter.messagebox
pygame.init()

# 设置登录窗口
win = Tk()
win.title('登陆')
win.geometry('300x150')
win.resizable(0, 0)
# 设置账号
Label(text='账号:').place(x=50, y=30)
uname = Entry(win)
uname.place(x=100, y=30)
# 设置密码
Label(text='密码:').place(x=50, y=70)
pwd = Entry(win)
pwd.place(x=100, y=70)
# 设置用户
users = {'123': '123'}


def sign():
    username = uname.get()
    password = pwd.get()
    users[username] = password


# 登陆
def login():
    username = uname.get()
    password = pwd.get()
    if username == 'abc' and password == '123':
        print('登陆成功')
        win.destroy()
    elif username in users and password == users[username]:
        print('登录成功！')
    else:
        print('账号或者密码错误')
        result = tkinter.messagebox.showerror(title='出错了！', message='账号或密码错误。')


# 登陆按钮
Button(text='注册', command=sign).place(x=150, y=110)
Button(text='登陆', command=login).place(x=100, y=110)


sore = 0
sore_font = pygame.font.SysFont("arial", 16)
caption_width = 500
caption_height = 500  # 设置窗口大小
white_color = (255, 255, 255)  # 设置白色的参数
blcak_color = (0, 0, 0)
game_title = '贪吃蛇'  # 设置游戏名称
cell = 10
snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]  # 蛇的初始位置
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]  # 食物初始随机位置
head_pos = [250, 250]  # 蛇头的位置
i1 = pygame.image.load('images/s1.png')    # 开始游戏字体
i1_1 = pygame.image.load('images/s1_1.png')
i2 = pygame.image.load('images/e1.png')
i2_1 = pygame.image.load('images/e1_1.png')    # 结束游戏字体
pygame.init()  # pygame的初始化,窗口通过pygame的初始化就可以使用它提供给的工具
caption = pygame.display.set_mode((caption_width, caption_height))  # 窗口
start_ck = pygame.Surface(caption.get_size())  # 充当开始界面的画布
start_ck.fill((255, 255, 255))  # 白色画布1（开始界面用的）
pygame.display.set_caption(game_title)  # 标题


def draw_rect(color, position):  # 将画图抽成一个方法
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))


def change_direction(head_pos):  # 将移动和加格抽成一个方法
    global food_pos
    global sore
    snake_init_pos.insert(0, list(head_pos))
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        sore += 1


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
                elif event.key == pygame.K_F1:
                    time.sleep(60)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if hit_the_self() or hit_the_wall(head_pos):
                pygame.quit()
        clock.tick(30)
        caption.fill(blcak_color)
        sore_text = sore_font.render('分数:%s' % str(sore), True, (250, 250, 250))
        caption.blit(sore_text, (10, 5))
        for pos in snake_init_pos:
            draw_rect(white_color, pos)
        draw_rect(white_color, food_pos)
        pygame.display.update()

# main()
n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if 0 <= x1 <= 150 and 0 <= y1 <= 50:
        start_ck.blit(i1_1, (0, 0))
        if buttons[0]:
            n1 = False
            win.mainloop()
            main()
    elif 0 <= x1 <= 150 and 100 <= y1 <= 150:
        start_ck.blit(i2_1, (0, 100))
        if buttons[0]:
            n1 = False
    else:
        start_ck.blit(i1, (0, 0))
        start_ck.blit(i2, (0, 100))
    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()
    caption.blit(start_ck, (0, 0))
    pygame.display.update()
