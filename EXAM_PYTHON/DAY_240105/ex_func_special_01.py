# -----------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (1)
# 매개변수의 개수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data ):
# - 가변인자 함수
# - 매개변수 개수 : 0개 ~ N개
# - 받아 온 data의 데이터 타입 : tuple (~ 컨테이너)
#   받아온 인수들 중 positional arguments (keyword arguments X)들을 모조리 담아서 tuple로 만든다.
# - C의 포인터와 관련 없음
# -----------------------------------------------------------

# 2개 정수를 덧셈 후 결과를 반환하는 함수 생성
def addTwo(num1, num2):
    return num1 + num2

# 5개 정수를 덧셈 후 결과를 반환하는 함수 생성
def addFive(a, b, c, d, e):
    return a + b + c + d + e

# ------------------------------------------------------------
# 함수 기능 : 전달받은 숫자를 모두 덧셈한 결과 반환
# 함수 이름 : addNumber
# 매개 변수 : *nums
# 반 환 값 : 계산결과
# -------------------------------------------------------------
def addNumber(*data):
    ret = 0
    for d in data:
        ret += d
    return ret

# 함수 사용 (함수 호출)
print(addNumber(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(addNumber(1, 2, 3))
print(addNumber(10))
print(addNumber())

# 인수로 넘길 때 *iterable/시퀀스 => 내부의 모든 원소를 하나씩 풀어서 전달 (Unpacking)
print(addNumber(*list(range(1, 11))))

a = [11, 22, 33, 44]
print(a)
print(*a, sep='-')
print()

aTuple = 'a', 'b', 'c'
print(aTuple)
print(*aTuple, sep='-')
print()

aDict = {'jj':'Hong', 'age':100}
print(aDict)
print(*aDict, sep='-')
print()
