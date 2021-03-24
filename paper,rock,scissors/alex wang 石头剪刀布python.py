import random
while True:
    a = input("请出拳(石头/剪刀/布)：")
    b = ["剪刀", "石头", "布"]
    # 定义赢的列表
    win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    # 计算机随机选择出拳
    mac = random.choice(b)
    print("你出拳：", a)
    print("计算机出拳：", mac)
    if a in b:
        if a == mac:
            print("平局")
        elif [a, mac] in win_list:
            # 如果在赢的列表中，代表你赢了，主要你和计算机的顺序要和赢的列表一样
            print("恭喜，你赢了")
        else:
            print("很遗憾，你输了")
    else:
        print("输入错误")

