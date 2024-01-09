'''
데이터를 메모리에 저장하는 방법
변수명 = 저장할 데이터
'''

name="홍길동"
name_99="홍길동"

# 메모리에 저장은 된다. -> 저장된 데이터 위치를 알 수 없음 -> 다시 사용 불가
2024
"Good Luck"

year=2024   # 2024 데이터가 저장된 주소를 year 이름이 붙은 메모리 저장
print(year)

# 데이터의 주소를 확인하는 내장함수 -> id( 실제 데이터 ) / id ( 변수명 )
print(id(2024))
print(id(year))

year=2023
print(id(year))

year=2024
print(id(year))

year='2024'
print(id(year))

# type(데이터) 또는 type(변수명)
print(type(2024))
print(type(4.))
print(type('4.'))