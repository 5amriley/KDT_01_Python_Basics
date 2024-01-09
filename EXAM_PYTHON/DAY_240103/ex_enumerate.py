# ----------------------------------------------------------
# for 요소 in 시퀀스/반복가능한객체:
# ==> for 인덱스 in range(len(변수명)):
# ==> 내장함수 enumerate()
# - (번호, 요소) 묶음으로 반환 함!!
# ----------------------------------------------------------
datas = ['Apple', 'Banana', 'Orange']

# 리스트 안에 요소 데이터 추출
for data in datas:
    print(data)

# 리스트 안에 요소 (인덱스, 데이터) 추출
for data in enumerate(datas, start=100):
    print(data)

x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

myDict = {}
for i, v in enumerate(x):
    # i=0, v='std01'
    myDict[v] = y[i]
print(myDict)