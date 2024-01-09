# [실습1] 알고 싶은 단을 입력 받고 해당 단을 출력해주세요.
dan = input("알고 싶은 단을 입력하세요 : ")
if dan:
    if dan.isdecimal():
        dan = int(dan)
        for i in range(1, 10):
            print(f'{dan} * {i} = {dan * i:2d}')
    else:
        print("숫자만 입력 가능합니다.")
else:
    print("입력한 데이터가 없습니다.")

# [실습2] 2단 ~ 9단까지 모두 출력하세요. 반복문 사용하기!
for x in range(2, 10):
    for y in range(1, 10):
        print(f'{x} * {y} = {x * y:2d}', end='  ')
    print()

# [실습3] 2단 ~ 9단까지 모두 출력하세요. 2단 3단 ... 9단 순으로 옆으로 연결되게 출력하세요.
for i in range(2, 10):
    print(f'---{i}단---', end='\t')
print()

for y in range(1, 10):
    for x in range(2, 10):
        # end 속성에 조건부 표현식 사용
        print(f'{x} * {y} = {x * y:<2d}', end='\n' if x==9 else '  ')
