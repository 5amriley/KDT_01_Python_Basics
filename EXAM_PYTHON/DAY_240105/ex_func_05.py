# ---------------------------------------------------------------
# 다양한 함수의 형태 - (4) 매개변수가 존재하지 않는 형태
# - 매개변수 : 함수에게 전달되는 데이터
# ---------------------------------------------------------------
# 함수 기능 : 인사메시지 출력
# 함수 이름 : welcome
# 매개 변수 : 없음
# 반 환 값 : 없음
# ---------------------------------------------------------------
def welcome():
    print("반가워요~ ^^")

# ---------------------------------------------------------------
# 함수 기능 : 프로그램 정보 출력
# 함수 이름 : printInfo
# 매개 변수 : 없음
# 반 환 값 : str
# ---------------------------------------------------------------
def printInfo():
    return "version 1.0\nDEVELOPER X\nEMAIL:master@game.com"

# 함수 사용 (함수 호출)
welcome()
welcome()

infoMsg = printInfo()
print(infoMsg)