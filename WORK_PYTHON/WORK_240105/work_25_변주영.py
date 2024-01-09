# [Unit 25. 딕셔너리 응용하기]

# 25.1.2 딕셔너리에 키와 기본값 저장하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')   # 'e': None 추가
print(x)

# 25.1.3 딕셔너리에서 키의 값 수정하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
print(x)
x.update(e=50)
print(x)

# 25.1.4 딕셔너리에서 키-값 쌍 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a')
print(x)

x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['d']
print(x)

# 25.1.6 딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.clear()
print(x)

# 25.1.7 딕셔너리에서 키의 값을 가져오기
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a'))

# 25.1.8 딕셔너리에서 키-값 쌍을 모두 가져오기
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(type(x.items()))
print(type(x.keys()))
print(type(x.values()))

# 25.5 딕셔너리의 할당과 복사
x = {'a':0, 'b':1, 'c':2, 'd':3}
y = x.copy()
print(x is y)   # 별개의 객체 (서로 영향을 주지 않는다)
print(x == y)   # 그러나 값은 동일하다. (일란성 쌍둥이?)

# 25.7 연습문제 : 평균 점수 구하기
maria = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(sum(maria.values()) / len(maria))

# 25.8 심사문제 : 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))

target_keys = []
for key, value in x.items():
    if value == 30: target_keys.append(key)
    if key == 'delta': target_keys.append(key)

for key in target_keys:
    del x[key]

print(x)
