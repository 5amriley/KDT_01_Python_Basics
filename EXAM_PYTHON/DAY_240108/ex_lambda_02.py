# 리스트 안의 모든 원소를 더한 합계 출력
datas = ['1', '4', '9']

for idx, d in enumerate(datas):
    datas[idx] = int(d)

# => 내장함수 map()
datas = list(map(int, datas))
print(datas)

# 리스트 안의 모든 원소에 * 100한 값을 리스트에 저장하기
def multiValue(x):
    return x * 100

datas1 = list(map(multiValue, datas))
print(datas1)

datas1 = list(map(lambda x: x * 100, datas))
print(datas1)
