# [Unit 14. else를 사용하여 두 방향으로 분기하기]

# 연습문제
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')

# 심사문제
korean, english, math, science = input().split()
korean = int(korean)
english = int(english)
math = int(math)
science = int(science)

if 0 <= korean <= 100 and 0 <= english <= 100 and \
    0 <= math <= 100 and 0 <= science <= 100:
    if korean + english + math + science >= 320:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 입력")
