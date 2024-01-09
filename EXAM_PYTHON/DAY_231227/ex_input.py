'''
표준입력기능의 내장함수 -> input()
- 문법 : input("요청메세지")
- 결과 : 입력 받은 데이터, 데이터 종류는 str
'''

# 이름을 입력 받기 -> input()
name = input("이름이 뭐니?")

# 입력 받은 데이터 출력하기 -> print()
print("당신 이름은 ", name, "이군요", sep="")
print(f"당신 이름은 {name}이군요")

# 숫자 2개를 입력 받기 -> input() 2개
number1 = input("정수 1개 입력 : ")
number2 = input("정수 1개 입력 : ")

print(number1, type(number1))
print(number2, type(number2))

# ---------------------------------------------------------------
# str -> int 타입으로 형변환 / 타입캐스팅 (Type Casting)
# - 함수 : 타입명( 데이터 )
#         int( 데이터 ) : 데이터를 int 타입으로 형변환된 값 반환
#         float( 데이터 ) : 데이터를 float 타입으로 형변환된 값 반환
#         str( 데이터 ) : 데이터를 str 타입으로 형변환된 값 반환
#         bool( 데이터 ) : 데이터를 bool 타입으로 형변환된 값 반환
# ---------------------------------------------------------------
# 입력받은 정수 2개를 정수로 타입 변환
number1 = int(number1)
number2 = int(number2)

print(number1, type(number1))
print(number2, type(number2))

# -------------------------------------------------------------
# 계산하기 -> 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# -------------------------------------------------------------
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")

# -------------------------------------------------------------
# 계산하기 -> 몫(//), 나머지(%)
# -------------------------------------------------------------
print(f"{number1} // {number2} = {number1 // number2}")
print(f"{number1} % {number2} = {number1 % number2}")

# -------------------------------------------------------------
# 계산하기 -> 제곱근(**)
# -------------------------------------------------------------
print(f"{number1} ** {number2} = {number1 ** number2}")
