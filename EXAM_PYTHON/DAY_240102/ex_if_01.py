# --------------------------------------------------------------------
# [요청] 키보드로 숫자를 입력받아서 입력받은 숫자만큼 *을 화면에 출력해주세요~
# [해결] (1) 숫자 입력 받기 => input()
#           str -> int 형변환
#       (2) 입력받은 숫자만큼 * 출력
#           '*' * 숫자
# ---------------------------------------------------------------------------
# (1) 숫자 입력 받기
num = input("정수 입력 : ")

# 입력받은 문자가 있는지 여부 : len(num)
if len(num) > 0:
    # str 숫자 -> int 숫자 형변환
    num = int(num)

    # (2) '*' 출력
    print('*' * num)
else:
    print("입력된 숫자가 없음")

# 조건에 상관없이 실행되는 코드
print("END")

'''
들여쓰기 : tab
내어쓰기 : shift + tab
'''
