import random

# 电脑人随机出拳
computer = random.randint(1, 3)

user = int(input('请出拳：1.拳头，2.剪刀，3.布'))

if computer == 1:
    computer = '拳头'
elif computer == 2:
    computer = '剪刀'
else:
    computer = '布'

if user == 1:
    user = '拳头'
elif user == 2:
    user = '剪刀'
else:
    user = '布'
print('电脑人出的是:%s,用户出的是:%s' % (computer, user))
if ((user == 1 and computer == 2)
        or (user == 2 and computer == 3)
        or (user == 3 and computer == 1)):
    print('恭喜用户胜出啦')
elif user == computer:
    print('好吧，这局是平局')
else:
    print('电脑人胜出！！！')
