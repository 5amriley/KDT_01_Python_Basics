# -------------------------------------------------------
# str 데이터 타입 전용함수, 즉, 메서드(Method) 살펴 보기
# - 메소드 (Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메서드명() ==> msg = "Good"
#                      msg.메서드명()
#   데이터.메서드명() ==> "Good".메서드명()
# -------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
# 왼쪽 -> 오른쪽, 제일 먼저 발견되는 문자의 인덱스를 반환
# 존재하지 않는 str 인덱스를 찾으면 Error 발생
data = "Merry Christmas"
print(f"data.index('C') -> {data.index('C')}")
print(f"data.index('r') -> {data.index('r')}")
print(f"data.index('r', 4) -> {data.index('r', 4)}")
print(f"data.index('r', data.index('r')+1) -> {data.index('r', data.index('r')+1)}")

first_r = data.index('r')
second_r = data.index('r', first_r + 1)
third_r = data.index('r', second_r + 1)
print(f'third_r : {third_r}')


# -----------------------------------------------------------
# str 데이터에서 문자열을 분리해주는 메서드 => split() 메서드
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str 분리
# - 반환값 : 여러 개의 str을 담아서 리스트(list)로 반환
# -----------------------------------------------------------
data = "Happy New Year"

datas = data.split()
print(type(datas), datas)

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print(f"datas[0] => {datas[0]}")

# split이 하나도 적용될 것이 없으면? 리스트에 통째로 담아서 반환
datas = data.split('-')
print(datas)

juminNo = '123456-1234567'
print(juminNo[:juminNo.index('-')], juminNo[juminNo.index('-')+1:])

juminNos = juminNo.split('-')
print(juminNos)
