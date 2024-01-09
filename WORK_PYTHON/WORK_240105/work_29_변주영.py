# [Unit 29. 함수 사용하기]

DEBUG = int(input("실행하려는 문제의 번호를 입력하세요 : "))    # 1: 연습문제, 2: 심사문제

# 연습문제
if DEBUG == 1:
    x, y = 10, 3

    def get_quotient_remainder(a, b):
        return a // b, a % b

    quotient, remainder = get_quotient_remainder(x, y)
    print(f'몫: {quotient}, 나머지 : {remainder}')


# 심사문제
if DEBUG == 2:
    x, y = map(int, input().split())

    def calc(num1, num2):
        """ 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환하는 함수"""
        return num1 + num2, num1 - num2, num1 * num2, num1 / num2

    a, s, m, d = calc(x, y)
    print(f'덧셈: {a}, 뺄셈: {s}, 곱셈: {m}, 나눗셈: {d:.1f}')
