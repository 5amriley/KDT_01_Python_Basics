'''
타입 캐스팅 (Type Casting) / 형변환
- 정수 -> 실수, 정수 -> 문자열, 정수 -> 논리
다른 데이터 타입으로 변환하는 것 (다른 타입 클래스의 생성자에 인수로 넘겨줌)
- 함수 : 데이터 타입명()
int(), float(), str(), bool()
'''
# int 데이터 타입으로 형변환 -------------------------------
# str -> int
print(int('200'), type(int('200')))
# print(int('200day')) # ValueError
# print(int('200.4')) # ValueError

# float -> int (소수점 이하 데이터 손실)
print(int(200.7), type(int(200.7)))

# bool -> int (False -> 0, True -> 1)
print(int(True), type(int(True)))
# print(int('True'))

# float 데이터 타입으로 형변환 -------------------------------
# str -> float
print(float('3.5'), type(float('3.5')))
print(float('35'), type(float('35')))
# print(float('0x123'))

# int -> float
print(float(45), type(float(45)))
print(float(-9), type(float(-9)))

# bool -> float
print(float(False), type(float(False)))
print(float(True), type(float(True)))
