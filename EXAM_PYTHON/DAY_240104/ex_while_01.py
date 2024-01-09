# ---------------------------------------------------------------------
# 반복문 - 2. while 문
# - 반복의 횟수가 정해지지 않은 경우에 사용
# - 반복의 횟수가 정해진 경우에도 사용 가능함
# - for와 달리 요소를 꺼내주지 않으므로, 인덱스를 사용해야 한다.
# -------------------------------------------------------------------
# [요청] 사용자로부터 좋아하는 음식명을 입력받아 주세요.
#       단, 가장 좋아하는 음식 5개만 입력받고, 출력하세요. (Top 5)
# print("가장 좋아하는 음식 5개를 입력하세요 :")
DEBUG1 = False  # flag 변수
if DEBUG1:
    fav_foods = []
    for i in range(5):
        fav_foods.append(input())

    print("당신은 ", end='')
    for food in fav_foods:
        print(food, end=', ' if fav_foods[-1] != food else '')
    print(" 를 좋아하는군요!")

DEBUG2 = True   # flag 변수
if DEBUG2:
    strFoods = ''
    for cnt in range(5):
        food = input(f'{cnt + 1}번째 좋아하는 음식명 입력 : ')
        strFoods = strFoods + food + (', ' if cnt != 4 else '')
    print('당신은', strFoods, "를 좋아하는 군요!")

# [요청] 사용자로부터 좋아하는 음식명을  입력받아 주세요.
#       단, 사용자가 '끝'이라는 음식명 입력 전까지 입력 받으세요.


# ------------------------------------------------------------------
# 기본 while 문법
# while 조건식:
# <--> 실행 코드
# <--> 실행 코드
# -------------------------------------------------------------------
# 타이머 프로그램 만들기 => 다운 카운팅 : 10 9 8 7 ... 1
downCnt = 10
while downCnt >= 1:
    print(downCnt, end=' ' if downCnt != 1 else '\n')
    downCnt -= 1

# 타이머 프로그램 만들기 => 업 카운팅 : 1 2 3 4 ... 10
upCnt = 1
while upCnt <= 10:
    print(upCnt, end=' ' if upCnt != 10 else '\n')
    upCnt += 1

for i in range(10, 0, -1):
    print(i, end=' ' if i != 1 else '\n')

for i in range(1, 11):
    print(i, end=' ' if i != 10 else '\n')

# [추가]
import time

for i in range(10, -1, -1):
    print(f'\r카운트 : {i}', end='')
    time.sleep(1)
