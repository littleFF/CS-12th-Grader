import random 
# 导入随机数模块
# 提示信息：输入的数字代表结果是什么
print('石头剪刀布游戏开始！玩家与人工智能小Q的对决，输入0代表剪刀、1代表石头、2代表布')

# 这里小Q代表了机器人

# 定义一个函数，用于判断输入的内容
def judge_inp(name, value):
    # 返回输入者的姓名，以及输入的值
    
    if value == '0': # 如果输入的是0 则打印剪刀
        print(name + "输入了剪刀")
        return 0 # 且返回0这个数字给输入者
    elif value == '1':
        print(name + "输入了石头")
        return 1
    elif value == '2':
        print(name + "输入了布")
        return 2
    return -1  # 只要输入内容不在判断内，就返回这个-1

# 开始一个无限循环，避免输入一次就结束掉了整个游戏
while True:
	# 获取玩家的输入
	user_inp = input('请玩家输入：')
	print() # 与打印内容换一行
	com_xq = random.randrange(0, 3)  # 小Q在0-3之间随机获取数字
	
	# 将玩家的名称，以及输入的内容放到函数里面判断，并拿到返回的值
	user_result = judge_inp('玩家',user_inp)
	
	# 如果返回的结果为-1，那么就说明玩家输入的内容不再范围内
	if user_result == -1:
	        print('输入错误，请重新输入\n')
	        continue  # 跳过这次循环，玩家重新输入
	
	# 将小Q的名称，以及输入的内容放到函数里面判断，并拿到返回的值
	# 由于判断时，是根据字符串判断，小Q产生的随机数为int类型，所以这里转换成str类型
	xq_result = judge_inp('小Q',str(com_xq))

	# 其中有一方胜利后，游戏结束！！
	if user_result == 0 and xq_result == 2:  # 玩家输入剪刀，小Q输入布
	    print('玩家赢了')
	    break
	elif xq_result == 0 and user_result == 2:  # 玩家输入布，小Q输入剪刀
	    print('小Q赢了')
	    break
	elif xq_result == 0 and user_result == 1:  # 玩家输入石头，小Q输入剪刀
	    print('玩家赢了')
	    break
	elif xq_result == 1 and user_result == 0:  # 玩家输入剪刀，小Q输入石头
	    print('小Q赢了')
	    break
	elif user_result == 1 and xq_result == 2:  # 玩家输入石头，小Q输入布
	    print('小Q赢了')
	    break
	elif user_result == 2 and xq_result == 1:  # 玩家输入布，小Q输入石头
	    print('玩家赢了')
	    break
	elif user_result == xq_result:  # 双方输入相同则为平局，开始下一剧
	    print('平局\n')