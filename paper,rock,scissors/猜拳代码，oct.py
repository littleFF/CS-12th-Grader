#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u'''
Created on 2019年3月7日

@author: wuluo
'''
__author__ = 'wuluo'
__version__ = '1.0.0'
__company__ = u'重庆交大'
__updated__ = '2019-03-07'

import random


class caiquan():
    print('欢迎来到猜拳游戏')
    print('进入游戏--8')
    print('退出游戏--9')
    b = input("请输入：")
    print("你的选择是: ", b)
    print("\n")
    while b == '8':
         print('请进行猜拳：')
         print('石头--0')
         print('布--1')
         print('剪刀--2')
         print('退出游戏--9')
         # 如果输入的数不是0,1,2；可以设置为重新输入，或者设置为失败
         a = random.randint(0, 2)
         b = int(input("你选择的是："))  # 整型，
         print("电脑选择的是：", a)
         if (a == 0 and b == 1) or(a == 1 and b == 2)or(a == 2and b == 0):
             print("你赢了！\n")
         elif a == b:
             print("平局！\n")
         else:
            print("你输了！\n")
    print('继续游戏--8')
    print('退出游戏--9')
    b = input("请重新选择：")
    print("你的选择是: ", b + "\n")


if __name__ == "__main__":
    caiquan()
    print('游戏结束！')
    pass