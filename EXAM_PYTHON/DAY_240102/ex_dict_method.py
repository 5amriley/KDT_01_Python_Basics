# -------------------------------------------------------------------
# dict 데이터 전용 함수, 즉, 메서드(Method)
# -------------------------------------------------------------------
# 빈 dict 타입 변수 생성
myDict = {}

# 데이터 추가 => myDict[키] = 데이터
myDict['one'] = 100

# 데이터 추가 => update(키=데이터) 메서드
# 주의!!! 키는 str 타입만 가능, str 타입이지만 '', "" 사용 안 됨
# myDict.update('two'=200) # ERROR
myDict.update(two=200, _1=1000)
print(myDict)

# 키만 추출해서 읽어오는 메서드 => keys() 메서드
keys = myDict.keys()
print(f'myDict 만의 키들 : {keys}, {type(keys)}')

# 값만 추출해서 읽어오는 메서드 => values() 메서드
values = myDict.values()
print(f'myDict 만의 키들 : {values}, {type(values)}')

# 키와 값을 추출해서 읽어오는 메서드 => o,ss() 메서드
items = myDict.items()
print(f'myDict 만의 키들 : {items}, {type(keys)}')

# 원소/요소 단위로 접근 위해서는 형변환 필요함!!
print(f'myDict 만의 키,값 묶음들 : {items}, {type(keys)}')

# 원소/요소 몯 삭제해주는 메서드 => clear()
myDict.clear()

# 키가 존재하지 않으면 None 반환
print(f'myDict.get("one") {myDict.get("one")}')

# --------------------------------------------------------------------
# 멤버 연산자 => 원소 in 여러개 저장 타입
#           => 원소 not in 여러 개 저장 타입
# - 여러개 저장 타입 : str, list, tuple, dict, set
# - 연산 결과 => True/False
# --------------------------------------------------------------------
aList = [1, 2, 3]
aTuple = 11, 22
aDict = {1:100, 2:100}

# 데이터/값 존재 여부
print(f'1 in aList : {1 in aList}')
print(f'1 in aTuple : {1 in aTuple}')
# 키 존재 여부
print(f'1 in aDict : {1 in aDict}')     # True (Key 존재)
print(f'1 in aDict : {100 in aDict}')   # False (Key 없음)
