#!GuessingNumer.py

# encoding = utf-8

import random

number_list = [1,2,3]  # 1: 石头,2:剪刀,3:布

guesture_list = ["石头","剪刀","布"]  # 1: 石头,2:剪刀,3:布

win_of_machine = 0 #机器赢局数

win_of_player = 0  #玩家赢局数

number_of_tries = 0

def guess():

    guesture_machine = random.choice(number_list)

    try:

      guesture_player = int(input("请猜手势(输入数字)：1-石头，2-剪刀，3-布\n"))

      if(guesture_player<1 or guesture_player >3):

          print("糊弄谁呢，请输入数字1、2或3！")

          return

    except:

      print("出错了,输入的不是数字!!")

      return

    global number_of_tries

    number_of_tries = number_of_tries + 1

    if guesture_machine == guesture_player:#平局

        print("恭喜你，猜对了.""机器出：",guesture_list[guesture_machine-1])

        global win_of_player

        win_of_player = win_of_player + 1

    else:

       print("对不起，猜错了。", "机器出：",guesture_list[guesture_machine-1])

       global win_of_machine

       win_of_machine = win_of_machine + 1

def display( ):

    print("***************************************************")

    print("********人机猜拳大赛-石头剪刀布********************")

    print("********玩法：机器出拳，玩家猜对手势赢，否则输*****")

    print("***************************************************")

    if(number_of_tries == 0):

       return

    print("玩家 VS 机器")

    print("局数: ", number_of_tries)

    print("比分：",win_of_player, ":",win_of_machine)

    if win_of_player > win_of_machine:

        print("好棒哦！继续努力.")

    else:

        print("加油！！！")

    print("***************************************************")

if(__name__ =="__main__"):

    while True:

        display()

        guess()



