import random

count = 3
while count:
    a = input("请出拳(石头/剪刀/布)：")
    b = ["剪刀", "石头", "布"]
    win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    mac = random.choice(b)
    print("你出拳：", a)
    print("计算机出拳：", mac)
    if a in b:
        count -= 1
        if a == mac:
            print("平局")
        elif [a, mac] in win_list:
            print("恭喜，你赢了")
            count += 1
        else:
            print("很遗憾，你输了")
    else:
        print("输入错误")

    print("你还剩余机会", count)
    if count == 0:
        print("机会用完啦，充值可以继续玩哦,充值金额分别为1,5,10元，一元可增加三次机会。")
        while True:
            a = input("请选择充值金额或者输入Q退出：")
            if a == 'Q':
                exit()
            try:
                a = int(a)
                if a == 1 or a == 5 or a == 10:
                    count = a
                else:
                    print("请输入1,5,10")
            except:
                print("请输入正确的金额")
				
