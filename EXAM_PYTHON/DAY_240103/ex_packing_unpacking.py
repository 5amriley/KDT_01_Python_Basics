# ---------------------------------------------------------------------
# 패킹 (Packing) & 언패킹 (Unpacking)
# --------------------------------------------------------------------------
msg = "Happy New Year"

# 패킹 방식
msgList = msg.split()
print(msgList[0], msgList[-1])

# 언패킹 방식
# 언팩할 데이터 수와 할당받는 변수 개수가 동일해야 함!!!
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 변수를 여러 개 생성하는 경우
age = 12
name = "Hong"
job = '학생'

# 튜플을 사용한 언패킹
age1, name1, job1 = 12, 'Hong', '학생'
print(age1, name1, job1)
