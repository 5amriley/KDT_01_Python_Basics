# -----------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# ------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산결과를 반환해주는 기능
# 함수 이름 : factorial
# 매개 변수 : 정수 1개
# 반 환 값 : 팩토리얼 결과
# -----------------------------------------------------
def factorial(the_num):
    result = 1
    if the_num < 0:
        result = -1 # 오류
    else:
        for i in range(1, the_num + 1):
            result *= i
    return result


# ------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산결과를 아래와 같은 형태로 반환하는 기능
#          예시 : '3! = 3 * 2 * 1 = 6'
# 함수 이름 : factorial2
# 매개 변수 : 정수 1개
# 반 환 값 : 팩토리얼 결과 문자열
# -------------------------------------------------------------
def factorial2(the_num):
    if the_num < 0:
        return '음수를 입력할 수 없습니다.'
    if the_num:
        sik = f'{str(the_num)}! = '
        for n in range(the_num, 0, -1):
            sik += str(n)
            sik += ' * ' if n != 1 else ' = '
        sik += str(factorial(the_num))
    else:
        sik = '0! = 1'
    return sik

print(factorial2(-10))
print(factorial2(0))
print(factorial2(5))
