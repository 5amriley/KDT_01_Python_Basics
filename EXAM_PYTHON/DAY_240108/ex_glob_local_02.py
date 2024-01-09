# ---------------------------------------------------
# 전역변수 (Global Variable)와 지역변수 (Local Variable)
# - 함수 내에서 전역변수 값을 변경하고자 하는 경우는 추가코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의 : 전역변수 값이 언제든지 함수로 변경될 수 있는 상황
#          사용 시에 주의 필요함
# ---------------------------------------------------
# 사용자 정의 함수 -------------------------------------
def currentDate(year, month, day):
    # year, month, day => 지역변수
    print(f"Today : {year}/{month:0>2}/{day:0>2}")

def currentDate2(month, day):
    # month, day => 지역변수
    # year => 전역변수
    # 함수 내에서 전역변수 값을 변경하고자 하는 경우는 global 예약어 사용
    global year
    year += 10
    print(f"Today : {year}/{month:0>2}/{day:0>2}")

def currentDate3(month, day, week):
    # month, day => 지역변수
    # year => 전역변수
    print(f"Today : {year}/{month:0>2}/{day:0>2}/{week}요일")

# 전역변수 ------------------------------------------
year, month, day = 2024, 1, 8

print(f'year : {year}, month : {month}, day : {day}')

currentDate2(month, day)

print(f'year : {year}, month : {month}, day : {day}')

# print(f'week : {week}') # 지역변수에 접근 못 함
