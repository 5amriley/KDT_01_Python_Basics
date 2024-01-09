# -------------------------------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력받은 데이터를 저장해 주세요.
# => 몇 번 입력할지 알 수 없음 ==> 무한 입력 받기
# => 종료 조건 ==> 사용자 'x' 입력
# -------------------------------------------------------------------------

DEBUG1 = False
while DEBUG1:
    data = input('저장하고 싶은 데이터 입력 (종료 x) : ')
    # 종료 검사
    # => break : 키워드가 있는 부분에서 바로 반복 종료, while문 안의 아래 코드 실행 안 됨
    if data in ['x', 'X']:
        print('종료')
        break
    print("OK")

# -----------------------------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력받은 정수만큼 알파벳을 출력
# [예시] 출력을 원하는 알파벳 수 입력 : 5
#       abcde
#       출력을 원하는 알파벳 수 입력 : 1
#       a
#       출력을 원하는 알파벳 수 입력 : 27
#       abcdefghijklmnopqrstuvwxyz 종료
#       출력을 원하는 알파벳 수 입력 : x
#       종료
# ----------------------------------------------------------------------
while True:
    count = input("출력 원하는 알파벳 수 입력 : ")

    # 무한 입력 반복 종료조건
    if count in ('x', 'X'):
        print('프로그램이 종료됩니다.')
        break   # 즉시 종료
    if count.isdecimal():
        count = int(count)

        aCode = ord('a')
        for value in range(count):
            value += aCode
            print(f'{value} {chr(value)}')
            if value == ord('z'): break
    else:
        print("정확한 데이터가 아닙니다.")

# [실습]
# for 반복문
isEnd = False
for n in range(100):
    if isEnd:
        print("프로그램을 종료합니다.")
        break

    print(f'out -> {n}')

    for n2 in range(100):
        if n2 > 10:
            isEnd = True    # flag 를 설정해서 바깥쪽 for 반복문도 종료되게 함
            break
        print(f"in -> {n2} ===> {n}번째")

# while 반복문
x = 0; isEnd = False
while x < 100:
    if isEnd:
        print("프로그램을 종료합니다.")
        break

    print(f"out -> {x}")

    y = 0
    while y < 100:
        if y > 10:
            isEnd = True
            break
        print(f"in -> {y} ===> {x}번째")
        y += 1
    x += 1

# [추가]
print('box' in 'boxyze')    # 'b' 'o' 'x' 'y' 'z' 'e' 까지 쪼갤 수 있음
print('bo' in ('boA', 'boC'))   # 'boA', 'boC' 가 원소 (더 쪼개서 생각하지 않음)
