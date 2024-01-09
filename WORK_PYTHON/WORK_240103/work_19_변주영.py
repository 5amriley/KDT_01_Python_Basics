# [Unit 19. 계단식으로 별 출력하기]

# 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

# 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

# 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

# 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 연습문제
for i in range(5):
    for j in range(5):
        if i > j:
            print(' ', end='')
        else:
            print('*', end='')
    print()

# 심사문제
height = int(input())

for i in range(1, height+1):
    for x in range(height-i):
        print(' ', end='')
    for y in range(1, 2 * i):
        print('*', end='')
    print()
