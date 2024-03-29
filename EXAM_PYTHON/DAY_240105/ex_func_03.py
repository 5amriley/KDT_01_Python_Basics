# ---------------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값 없는 함수
# ---------------------------------------------------------------
# 함수 기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
# 반 환 값 : 없음
# ---------------------------------------------------------------
def addTwo(x, y):
    value = x + y
    print(f'{x}+{y}={value}')

# 함수 사용 (함수 호출)
addTwo(10, 3)

# 함수 호출 시에 매개변수 개수와 동일하게 데이터를 전달해야 함! -----------
# ERROR
# addTwo(10, 5, 3)
# addTwo(10)
# --------------------------------------------------------------

# --------------------------------------------------------------
# 함수 기능 : 문자열을 대문자로 변환해주는 기능
# 한수 이름 : convertCase
# 매개 변수 : word
# 반 환 값 : 없음 => 아무 것도 바뀌지 않음 => return 해줘야 함
# --------------------------------------------------------------
def convertCase(word):
    word = word.upper()
    return word


# --------------------------------------------------------------
# 함수 기능 : 시퀀스 객체의 모든 원소를 대문자로 변환해주는 기능
# 한수 이름 : convertCase
# 매개 변수 : str 타입의 원소로 구성된 list
# 반 환 값 : 없음
# --------------------------------------------------------------
def convertCase2(dataList):
    # for idx in range(len(dataList)):
    #     dataList[idx] = dataList[idx].upper()
    # print(dataList)

    for idx, data in enumerate(dataList):
        dataList[idx] = data.upper()
    print(dataList)


# 함수 사용,
datas = ['Apple', 'Banana', 'Mango']

print(f'[BF] {datas}')
convertCase2(datas)
print(f'[AF] {datas}')

datas[0] = convertCase(datas[0])

# 리스트는 메모리에 주소가 저장되어 있기 때문에 매개변수에도 주소가 복사되어,
# 함수 안에서 바꾸어도 똑같은 객체가 바뀐다.
# 문자열은 ~~