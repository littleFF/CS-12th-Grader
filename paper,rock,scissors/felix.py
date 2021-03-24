
import random
# 出拳
while True:
    punches = ['石头','剪刀','布']
    computer_choice = random.choice(punches)
    user_choice = ''
    user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
    while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
        print('输入有误，请重新出拳')
        user_choice = input()
    # 亮拳
    print('————战斗过程————') 
    print('电脑出了：%s' % computer_choice) 
    print('你出了：%s' % user_choice)
    # 胜负
    print('—————结果—————') 
    if user_choice == computer_choice:  # 使用if进行条件判断
        print('平局！') 
    elif (user_choice == '石头' and computer_choice == '剪刀') or (user_choice == '剪刀' and computer_choice == '布')or (user_choice == '布' and computer_choice == '石头'):
        print('你赢了！') 
    else:
        print('你输了！')
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：') 
    if a1 == 'n':
        print('\n【结束游戏】') 
        break 