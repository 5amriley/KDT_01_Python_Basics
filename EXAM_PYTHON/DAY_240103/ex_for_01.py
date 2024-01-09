# 1~100 범위에서 2의 배수에 해당한 정수로 리스트 생성
result = list(range(2, 101, 2))

# "24681012...100"
# result = str(result) # 리스트에 str() 하면 원하는 결과 X

# int -> str 형변환
strNum = ''
for num in result:
    strNum += str(num)
print(strNum)

# 리스트 안의 모든 요소를 str 타입으로 변환해서 저장
# 데이터의 인덱스 범위 : 0 ~ len(data) -1
print(f'[BEFORE] result : {result}')

for idx in range(len(result)):
    result[idx] = str(result[idx])

print(f'[AFTER] result : {result}')
