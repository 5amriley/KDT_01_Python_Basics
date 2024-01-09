# [Unit 17. while 반복문으로 ~~~]

# 입력한 횟수대로 반복하기
cnt = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < cnt:
    print('Hello, world!', i)
    i += 1

# 반복 횟수가 정해지지 않은 경우
import random

i = 0
while i != 3:
    # 주사위의 수가 3이 나올 때까지 반복
    i = random.randint(1, 6)
    print(i)

# while 반복문으로 무한루프 만들기
'''
while 1:
    # 콘솔(터미널, 명령 프롬프트)에서 ctrl + c 를 입력하여 무한루프를 종료
    print('Hello, 1!')
'''

'''
while 'Hello':
    # 콘솔(터미널, 명령 프롬프트)에서 ctrl + c 를 입력하여 무한루프를 종료
    print('Hello, world!')
'''

# 연습문제
i, j = 2, 5

while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

# 심사문제
balance = int(input())
fare = 1350

while balance >= fare:
    balance -= fare
    print(balance)
