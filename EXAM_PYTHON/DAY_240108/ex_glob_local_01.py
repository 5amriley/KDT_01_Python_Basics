# ---------------------------------------------------
# 전역변수 (Global Variable)와 지역변수 (Local Variable)
# 전역변수 (Global Variable)
# - 파이썬(py) 파일에 존재하는 변수
# - 파일 내부 모든 곳에서 사용 가능한 변수
# - 파일 실행을 종료하면 메모리에서 사라짐
# 지역변수 (Local Variable)
# - 함수에 존재하는 변수
# - 함수에서만 사용가능한 변수
# - 함수가 종료되면 변수들은 메모리에서 사라짐
# ---------------------------------------------------
# Python Tutor 실습
# User defined function ------------------------------
def addTwo(n1, n2):
    print(n1+n2)

def currentDate(year, month, day):
    year += 10
    month += 10
    day += 10

# Global variable -----------------------------------
year = 2024
month = 1
day = 8

# Calling function ----------------------------------
addTwo(2, 5)

currentDate(year, month, day)

# print current variable ----------------------------
print("Current", year, month, day)
