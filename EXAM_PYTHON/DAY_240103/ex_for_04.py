# --------------------------------------------------------------------
# 반복문과 내장함수 => map(), zip()
# --------------------------------------------------------------------
xList = ['1', '3', '5', '7']

# xList 안 모든 원소를 정수 int로 바꿔주세요
for idx in range(len(xList)):
    xList[idx] = int(xList[idx])
print(xList)

# ------------------------------------------------------------------
# 시퀀스 또는 반복이 가능한 객체의 요소에 적용후 값을 다시 저장해야 하는 경우
# 자주 사용되는 기능이라, 내장함수로 제공 => map()
# - 문법 : map(함수명, 시퀀스 또는 반복 가능한 객체)
# ------------------------------------------------------------------
# int 요소인 xList를 str요소로 변환
result = list(map(str, xList))
print(result)

# --------------------------------------------------------------------
# list 데이터를 dict 데이터로 생성
# --------------------------------------------------------------------
x = ['std01', 'std02', 'std03']
y = [90, 100, 95]

# 방법 (1) -> 직접 할당
xyDict = {}
xyDict['std01'] = 90
xyDict['std02'] = 100
xyDict['std03'] = 95

print(xyDict)

# 방법 2 -> for 반복문
xyDict2 = {}
for idx in range(len(x)):
    xyDict2[x[idx]] = y[idx]

print(xyDict2)

# 방법 3 -> dict( [(키, 값), (키, 값), ... ] ) 생성자 함수
tuple_entry = []
for idx in range(len(x)):
    tuple_entry.append((x[idx], y[idx]))
xyDict3 = dict(tuple_entry)
print(xyDict3)

# 방법 4 -> dict( [(키, 값), (키, 값), ... ] ) 생성자 함수
# zip() 함수
xyDict4 = dict(zip(x, y))
print(xyDict4)
