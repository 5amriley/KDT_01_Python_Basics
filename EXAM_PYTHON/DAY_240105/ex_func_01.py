# -----------------------------------------------------------------
# 함수 (Function)
# - 특정 기능을 구현하기 위한 코드 묶음을 의미
# - 자주 사용되는 기능을 함수로 구현함
# - 함수 생성 문법
#   def 함수명(매개변수1, 매개변수2, ..., 매개변수):
#       실행코드
#       실행코드
#       return 반환값  <-- 결과값, 리턴값
# -----------------------------------------------------------------
# 함수기능 : 숫자 2개의 합계를 계산 후 결과를 반환해주는 기능
# 함수이름 : addTwo
# 매개변수 : x, y
# 반환값  : x + y
# -----------------------------------------------------------------
def addTwo(x, y):
    value = x + y
    return value


# -----------------------------------------------------------------
# 함수기능 : 숫자 2개의 곱셈 결과를 계산 후 결과를 반환해주는 기능
# 함수이름 : mulTwo
# 매개변수 : x, y
# 반환값  : x * y
# -----------------------------------------------------------------
def mulTwo(x, y):
    value = x * y
    return value


# ----------------------------------------------------------------
# 함수 사용 => 함수 호출 (Calling)
# 방법 : 함수이름(데이터, 데이터, ...)
# --------------------------------------------------------------
print(mulTwo(3, 10))
print(mulTwo(5, 2))
print(mulTwo(7, 4))
