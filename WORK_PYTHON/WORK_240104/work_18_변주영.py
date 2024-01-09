# [Unit 18. break, continue로 반복문 제어하기]

# 연습문제: 3으로 끝나는 숫자만 출력하기
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

# 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
while True:
    start, stop = map(int, input().split())

    if 1 <= start <= 200 and 10 <= stop <= 200 and start < stop:
        break
    else:
        print('범위가 맞지 않습니다. 다시 입력하세요.')

i = start

while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1
