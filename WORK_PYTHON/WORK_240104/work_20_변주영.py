# [Unit 20. FizzBuzz 문제]

# FizzBuzz 문제
for i in range(1, 101):
    fb = ""
    if i % 3 == 0:
        fb += "Fizz"
    if i % 5 == 0:
        fb += "Buzz"
    if len(fb) != 0:
        print(fb)
    else:
        print(i)

# 연습문제: 2와 11의 배수, 공배수 처리하기
for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)

# 심사문제: 5와 7의 배수, 공배수 처리하기
while True:
    start, stop = map(int, input().split())
    if 1 <= start <= 1000 and 10 <= stop <= 1000 and start < stop:
        break
    else:
        print('조건에 맞지 않습니다. 다시 입력하세요.')

for i in range(start, stop+1):
    if i % 5 == 0 and i % 7 ==0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
