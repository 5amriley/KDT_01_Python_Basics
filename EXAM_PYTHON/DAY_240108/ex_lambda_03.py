# -----------------------------------------------------
# filter(함수명, 반복가능객체)
# - 조건에 맞는 데이터만 반환
# -----------------------------------------------------
# 예) 5초과 10미만 데이터만 추출
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
a = list(filter(lambda x: 5<x<10, a))
print(a)

# import random # random.py 파일에 있는 모든 변수, 함수, 클래스 가져오기
from random import randint, random # random.py 파일에서 randint, random 함수만 가져오기
r = randint(1, 10)

from functools import reduce
print(reduce(lambda x, y: x+y, a))
