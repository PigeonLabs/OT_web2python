#NUUMBER
print(30//4) # 몫
print(30%4) # 나머지
print(abs(-30.272)) # 절댓값


#STRING
print("Hello \"the\" world!") # 역슬래시 다음은 문자열로 처리
print("Hello world!\b?") # \b 백스페이스
print("Hello\nworld!") # \n 줄바꿈
print("Hello\tworld!") # \t 탭
print("Hello\vworld!") # \v 수직탭
print('''Hello
World''') # 여러줄 - 줄바꿈 주의

a = "Hello world!"
print(len(a)) # 자릿수세기
print(a[4]) # 다섯번째 문자 추출
print(a[-1]) # 마지막 문자 추출
print(a[0:5]) # 첫번째부터 다섯번째까지(여섯번째 전까지) 추출
print((a+"\n")*2) # 두번 반복 with 줄바꿈

name = 'SJ'
lorem = '''To '''+name+''', Do consectetur fugiat adipisicing qui proident enim consectetur.
'''+name+''' Cillum minim ullamco ut voluptate veniam anim fugiat proident elit eu.
Duis sunt non irure laboris minim nisi aute nostrud non.
Occaecat do enim commodo irure amet minim reprehenderit irure consequat cupidatat eiusmod consectetur.
'''+name+''' de occaecat mollit in in amet. Reprehenderit magna dolor esse nisi.'''
print(lorem)

age = 24
print('''To {name} age {age:d}, Do consectetur fugiat adipisicing qui proident enim consectetur.
{name} Cillum minim ullamco ut voluptate veniam anim fugiat proident elit eu.
Duis sunt non irure laboris minim nisi aute nostrud non.
Occaecat do enim commodo irure amet minim reprehenderit irure consequat cupidatat eiusmod consectetur.
{name} de occaecat mollit in in amet. Reprehenderit magna dolor esse nisi.'''.format(name=name, age=age)) # age:d 로 포맷코드 지정(digit) // age = "24" 처럼 값이 string으로 들어가면 에러


#BOOLEAN - T/F
print(1==1) # True
print(1==2) # False
print(1<2) # True
print('world' in "Hello world!") # True

import os
print(os.listdir(os.getcwd()))
print(os.path.exists("ex.py")) # True

print(not True) # False

# AND - 모두 만족해야..
print(True and True) # True
print(True and False) # False
print(False and False) # False

#OR - 하나라도 만족하면..
print(True or True) # True
print(True or False) # True
print(False or False) # False


#LIST
squares = [1, 'four', 9, 16, 25]
print(squares)
print(squares[-3:]) # 뒤에서부터 3번째 데이터부터~
print(len(squares))
squares[1] = 4 # element replacement
del squares[4] # delete element
squares.append(36) # append element
print(squares)

#DICTIONARY
person = {'name':'SJ', 'address':'gangnam-gu'}
print(person['name'])

#SET
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2) # 집합이므로 원소 중복 불가


#LOOP
import random
#정확한 횟수로 반복하고 싶을 때 - FOR
for value in ['a','b','c']: print(value)
for value in range(10): print(value) # 0부터 9까지
#조건 만족시까지 - WHILE
i=0
while float(i)<0.9: # random하게 생성된 소수가 0.9보다 클때 멈춤
    i=random.random()
    print(i)


#FUNCTION
def average(av1,av2,av3):
    return (av1+av2+av3)/3

print(average(1,3,5))


