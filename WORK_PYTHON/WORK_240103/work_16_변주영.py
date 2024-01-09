# [Unit 16. for 반복문으로 ~~~]

# 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(5, 12):
    print('Hello, world!', i)

# 증가폭 사용하기
for i in range(0, 10, 2):
    print('Hello, world!', i)

# 숫자를 감소시키기
for i in range(10, 0):
    # 실행 안 됨
    print('과연?', i)

for i in range(10, 0, -1):
    # 실행 됨
    print('이건?', i)

for i in reversed(range(10)):
    print('거꾸로?', i)

# 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')
print()

for letter in reversed('Python'):
    print(letter, end=' ')
print()

# 연습문제
x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    print(i * 10, end=' ')
print()

# 심사문제
dan = int(input())

for i in range(10):
    print(f'{dan} * {i} = {dan * i}')
