# ----------------------------------------------------------
# list 의 원소/요소 데이터 변경 및 삭제
# ----------------------------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 갖는 리스트를 생성하기
happy_list = list("Merry Christmas")
print(f'happy_list -> {happy_list}')

# 리스트에서 ' ' 데이터를 '***'로 변경
happy_list[5] = "***"
print(f'happy_list -> {happy_list}')

# 삭제 => del(데이터) 또는 del 데이터
del happy_list[5]
print(f'happy_list -> {happy_list}')

del happy_list
# print(happy_list) # 접근 안 됨
