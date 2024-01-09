# [Unit 13. 딕셔너리 사용하기]

# if 조건문에서 코드를 생략하기
x = 10
if x == 10:
    pass

# if 조건문과 들여쓰기
x = 10

if x == 10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

# 중첩 if 조건문 사용하기
x = 15

if x >= 10:
    print('10 이상입니다.')
    if x == 15:
        print('15입니다.')
    if x ==20 :
        print('20입니다.')

# 사용자가 입력한 값에 if 조건문 사용하기
x = int(input())

if x == 10:
    print('10입니다.')

if x == 20:
    print('20입니다.')

# 연습문제
x = 5

if x != 10:
    print('ok')

# 심사문제
original_price = int(input())
coupon_name = input()

if coupon_name == "Cash3000":
    print(original_price - 3000)
elif coupon_name == "Cash5000":
    print(original_price - 5000)
