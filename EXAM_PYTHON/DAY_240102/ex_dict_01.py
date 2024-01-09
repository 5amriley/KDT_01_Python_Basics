# ------------------------------------------------------------------
# [질문] 5명 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
# --------------------------------------------------------------------
# 방법1) 학번 변수 5개, 학점 변수 5개

# 방법2) 학번 리스트 1개, 학점 리스트 1개

# 방법3) 학번03번 학생의 학번과 점수를 철룩
# 한 리스트에서 인덱스를 얻고, 그 인덱스를 사용하여 다른 리스트에서 인덱싱

# ---------------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형태 => 키 : 데이터 (예: 주민번호:이름, 학번:전공)
# - 조건 => 키가 중복되면 안 됨!
# - 문법 => { 키1:데이터1, 키2:데이터2, ... , 키N:데이터N }
# ----------------------------------------------------------------------
stdNumsJumsu = {'std01':90, 'std02':89, 'std03':100, 'std04':76, 'std05':34}
print(f'stdNumJumsu : {type(stdNumsJumsu)}, {stdNumsJumsu}')

# 원소 읽는 방법 => 변수명[키]
print(f'stdNumsJumsu["std03"] : {stdNumsJumsu["std03"]}')

# 마지막 원소 지정하는 -1 사용 => -1에 대한 키가 없으면 ERROR
# print(f'stdNumJumsu[-1] : {stdNumsJumsu[-1]}')

# ----------------------------------------------------------------------
# 원소 / 요소 추가 방법 => 변수명[새로운 키] = 데이터
# ----------------------------------------------------------------------
# 학번 10인 학생의 점수 99.8 저장, 즉, 추가하기
stdNumsJumsu['std10'] = 99.8
print(f'stdNumJumsu : {type(stdNumsJumsu)}, {stdNumsJumsu}')

# ----------------------------------------------------------------------
# 원소 / 요소 변경 => 변수명[새로운 키] = 새로운 데이터
# ----------------------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdNumsJumsu['std10'] = 99
print(f'stdNumJumsu : {type(stdNumsJumsu)}, {stdNumsJumsu}')

# ----------------------------------------------------------------------
# 원소 / 요소 삭제 => del 변수명[키] 또는 del(변수명[키])
# ----------------------------------------------------------------------
del stdNumsJumsu['std10']
print(f'stdNumJumsu : {type(stdNumsJumsu)}, {stdNumsJumsu}')
