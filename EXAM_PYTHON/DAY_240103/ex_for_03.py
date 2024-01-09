# [실습] ----------------------------------------------------------
# - 문자열 여러 개와 실수 여러 개를 입력 받기 -> input() 1개만 사용
# - 첫 번째 입력받은 값은 Key
# - 두 번째 입력받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# ----------------------------------------------------------------
data = input("문자열과 실수 여러 개 입력\n단, 문자열과 실수 갯수 동일\
(예: aa bb cc, 1.1 2.2 3.3)")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 "  ,  " 문자열 안에 ',' 존재해야 함
# - (2) 문자열과 실수 개수가 동일해야 함
if ',' in data:
    keys, values = data.split(',')
    keys = keys.split()
    values = values.split()

    dataDict = {}
    dataDict2 = {}
    if len(keys) == len(values):
        for num in range(len(keys)):
            dataDict[keys[num]] = float(values[num])
        dataDict2 = dict(zip(keys, values))

        print(dataDict)
        print(dataDict2)
    else:
        print("정확한 형식이 아닙니다.")
else:
    print("정확한 형식이 아닙니다.")

# -------------------------------------------------------------
# 내장함수 zip => 같은 인덱스끼리 묶는다.
# -------------------------------------------------------------
x = [1, 2, 3, 4, 5]
y = [11, 22, 33, 44, 55]
z = [111, 222, 333, 444, 555]

result = list(zip(x, y, z))
print(result)
