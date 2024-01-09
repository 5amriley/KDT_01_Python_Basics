# -----------------------------------------------------------------
# 컴프리헨션 (Comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension
# - 메모리 사용량, 속도 측면에서 for문 보다 더 유리
# --------------------------------------------------------------------
# [실습1] aList의 요소 값을 제곱한 값을 원소로 가지는 bList를 생성하세요
aList = [1, 2, 3, 4]
bList = []

# 일반적인 for 방식
for a in aList:
    bList.append(a ** 2)
print(bList)

# 컴프리헨션 방식
cList = [ a ** 2 for a in aList ]
#         ------ --------------
#          (2)         (1)
print(cList)

# [실습2] aList의 요소 값 중에서 짝수인 데이터만 제곱한 값을 요소로 가지는 bList 생성하세요
# 일반적인 for 방식
bList2 = []
for a in aList:
    if not a % 2:
        bList2.append(a ** 2)
print(bList2)

# 컴프리헨션 방식
cList2 = [ a ** 2 for a in aList if not a % 2 ]
#          ------ -------------- ------------
#           (3)         (1)          (2)
print(cList2)

# [실습3] aList의 요소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 저장한 bList 생성하세요
# 일반적인 for 방식
bList3 = []
for a in aList:
    if not a % 2:
        bList3.append(a ** 2)
    else:
        bList3.append(a)
print(bList3)

# 컴프리헨션 방식
cList3 = [ a ** 2 if not a % 2 else a for a in aList ]
#          ------ ------------ ------ --------------
#          (3-T)       (2)      (3-F)      (1)
print(cList3)
