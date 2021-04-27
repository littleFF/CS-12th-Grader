import random
while 1:
 s=int(random.randint(1,3))
 print(s)
 print()
 if s==1:
  ind="stone"
 elif s==2:
  ind="scissors"
 elif s==3:
  ind="paper"
 m=input('Please input your option,if you input the end, this game will be end. ')
 blist=['stone','scissors','paper']
 if (m not in blist) and (m!='end'):
  print('your input is wrong and please input the right option again or end the game: ')
 elif (m not in blist) and (m=='end'):
  print('the game is ending now...')
  break
 elif m==ind:
  print('draw')
 elif (m=='stone' and ind=='scissors') or (m=='paper' and ind=='stone') or (m=='scissors' and ind=='paper'):
  print('you win this game')
 elif (m=='stone' and ind=='paper') or (m=='paper' and ind=='scissors') or (m=='scissors' and ind=='stone'):
   print( 'you loss this game')
