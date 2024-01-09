# --------------------------------------------------------
# 람다 표현식 또는 람다 함수
# - 익명 함수(anonymous function)라고도 함!
# - 짧은 코드의 함수 또는 반복해서 재사용이 많이 않은 코드의 경우 사용
# - 문법 : lambda 매개변수1, ... , 매개변수N : 표현식
# - 결과 : 매개변수를 활용한 표현식 결과 값이 lambda 위치에 반환됨
# -----------------------------------------------------------
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

print((lambda a, b: a+b)(4, 5))
print((lambda a, b: a-b)(4, 5))

my_add = lambda a, b: a+b
my_minus = lambda a, b: a-b

print(my_add(4, 5))
print(my_minus(4, 5))
