# [Unit 26. 세트 사용하기]

# 26.1.1 세트에 특정 값이 있는지 확인하기
fruits = ['strawberry', 'grape', 'orange', 'pineapple', 'cherry']
print('orange' in fruits)

# 26.1.2 set를 사용하여 세트 만들기
a = set('apple')    # 유일한 문자만 세트로 만듦, 중복된 문자 제외
print(a)

b = set(range(5))
print(b)

c = set()   # 빈 세트
print(c)

d = set('하하하')
print(d)

# 26.2 집합 연산 사용하기
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(set.union(a, b))

print(a & b)
print(set.intersection(a, b))

print(a - b)
print(set.difference(a, b))

# 대칭차집합 ((A-B)+(B-A), XOR)
print(a ^ b)
print(set.symmetric_difference(a, b))

# 26.2.1 집합 연산 후 할당 연산자 사용하기
# |= : 합집합 -> 할당
# &= : 교집합 -> 할당
# -= : 차집합 -> 할당
# ^= : 대칭차집합 -> 할당

# 26.2.2 부분집합과 상위집합 확인하기
# > >=
# < <=

# 26.2.3 세트가 같은지 다른지 확인하기
# == !=

# 26.2.4 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 5, 6}))

# 26.3 세트 조작하기
# 26.3.1 세트에 요소를 추가하기
a = {1, 2, 3, 4}
a.add(5)
print(a)

# 26.3.2 세트에서 특정 요소를 삭제하기
a = {1, 2, 3, 4}
a.remove(4)
print(a)

# 26.3.3 세트에서 임의의 요소를 삭제하기
a = {1, 2, 3, 4}
a.pop()
print(a)

# 26.3.4 세트의 모든 요소를 삭제하기
a = {1, 2, 3, 4}
a.clear()
print(a)

# 26.4 세트의 할당과 복사
a = {1, 2, 3, 4}
b = a.copy()
print(a is b)
print(a == b)

# 26.5 반복문으로 세트의 요소를 모두 출력하기
a = {1, 2, 3, 4}
for i in a:
    print(i)

# 26.6.1 세트 표현식에 if 조건문 사용하기
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)

# 26.8 연습문제 : 공배수 구하기
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a & b)

# 26.9 심사문제 : 공약수 구하기
a, b = map(int, input().split())

a_div = {i for i in range(1, a+1) if a % i == 0}
b_div = {i for i in range(1, b+1) if b % i == 0}

common_div = a_div & b_div

print(sum(common_div))
