# [Unit 22. 리스트와 튜플 응용하기]

# 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(500)
print(a)

# 리스트 안에 리스트 추가하기 (리스트가 통째로 원소로 추가)
a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

# 리스트 확장하기 (리스트 대 리스트로 대등하게 합쳐진다.)
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

# 리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

# 리스트 특정 인덱스의 요소를 삭제하기 (pop - 마지막 인덱스)
a = [10, 20, 30]
print(a.pop())
print(a)

# 리스트에서 특정 값을 찾아서 삭제하기 (remove)
a = [10, 20, 30]
a.remove(20)
print(a)

# 리스트의 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)

a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)

# 리스트의 모든 요소를 삭제하기
a = [10, 20, 30]
a.clear()
print(a)

# 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]
print(a)

# 리스트 표현식에서 for 반복문과 if 조건문을 여러 번 사용하기
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

# 리스트에 map 사용하기
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

# input().split() 과 map()
x = input().split()
m = map(int, x)
a, b = m
print(a, b)

# 연습문제 : 리스트에서 특정 요소만 뽑아내기
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo',\
     'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 심사문제 : 2의 거듭제곱 리스트 생성하기
start, finish = map(int, input().split())
exponents = list(range(start, finish+1))
del exponents[1]
del exponents[-2]
result = [2 ** ex for ex in exponents]
print(result)
