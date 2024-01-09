# ------------------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (2)
# - 매개변수의 개수를 유동적으로 가변으로 하는 함수
# - 키와 값의 덩어리 데이터
# - 형태 : def 함수명( **data ):
# - 가변 인자 함수
# - 매개변수 개수 : 0개 ~ N개
# - 호출: 함수명(키1=값1, 키2=값2, ... , 키N:값N)
#        함수명(키1=값1)
#        함수명()
# [주의] 키값을 str으로 하면 안 됨 (따옴표 X)
#       함수 인수 입력형식은 '변수=값' 형태라서..? 키로 저장될 때 어차피 문자열로 저장돼서?
# [주의] 키워드 파라미터는 positional arguments 뒤에 위치해야 한다. (앞쪽에 있으면 어디까지가 키워드 파라미터인지 모르므로)
# ------------------------------------------------------------------
aDict={'name':'Hong', 'age':10}
aDict.update(job='학생')
aDict.update(job='학생', birth='1112', blood='A')
print(aDict)
aDict.update(점수1=100, 점수2=200, 점수3=300, 점수4=400, 점수5=500)
print(aDict)

# ------------------------------------------------------------
# 함수 기능 : 회원 가입
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ...
#           가변 + 데이터 정보 함께
#           키워드파라미터 **member
# 반 환 값 : '가입 완료되었습니다' str
# -------------------------------------------------------------
def joinMember(**member):
    # 넘겨진 값들을 받아서 member 라는 이름의 딕셔너리로 만들어 쓰겠다.
    print(member)
    # 멤버 저장소에 멤버 추가하기
    #members[f'M{len(members)}'] = member
    members.update(**member)


# 함수 사용 (함수 호출)
members = {}    # 가입된 회원들 저장 변수

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='2020,10,10')
joinMember(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
joinMember(id='baby', birth='2024/01/01', blood='A')

print(f'[AF] : {members}')

# m = {'name':'Hong', 'age':17}
# print(m.keys)
# print(m.values())
# print(m.items())


# ------------------------------------------------------------
# 함수 기능 : 회원 가입
# 함수 이름 : joinMember2
# 매개 변수 : 필수 => id, pw
#           선택 => **option => 이름, 전화번호, 아이디, 이메일, 주소, 생일, ...
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료되었습니다' str
# -------------------------------------------------------------
def joinMember2(id, pw, **option):
    print('OK')

joinMember2('h', 'ph')


# ------------------------------------------------------------
# 함수 기능 : 회원 가입
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw, loc(default), gender(default)
#           선택 => **option => 이름, 전화번호, 아이디, 이메일, 주소, 생일, ...
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료되었습니다' str
# -------------------------------------------------------------
def joinMember3(id, pw, loc='내국인', gender='남자', **option):
    print(id, pw, loc, gender)

joinMember3('h', 'ph')
joinMember3('h', 'ph', gender='여자')
joinMember3('h', 'ph', phone='010-1111-0000', blood='A')