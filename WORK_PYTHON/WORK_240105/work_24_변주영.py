# [Unit 24. 문자열 응용하기]

# 24.1.1 문자열 바꾸기
greeting = 'Hello World'
print(greeting.replace('W', 'w'))
print(greeting)

# 24.1.12 양쪽의 특정 문자 삭제하기
print('.Python,'.strip(',.'))   # 문자열 양쪽의 ,(콤마)와 .(점) 삭제

# 24.1.13 문자열을 왼쪽 정렬하기
# ljust(길이) : 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬, 남는 공간을 공백으로 채운다.
print('Python'.ljust(10))

# 24.1.14 문자열을 오른쪽 정렬하기
# rjust(길이) : 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬, 남는 공간을 공백으로 채운다.
print('Python'.rjust(10))

# 24.1.15 문자열을 가운데 정렬하기
# center(길이) : 문자열을 지정된 길이로 만든 뒤 가운데로 정렬, 남는 공간을 공백으로 채운다.
print('Python'.center(10))

# 24.1.16 메서드 체이닝 (method chaining)
print('python'.rjust(10).upper())

# 24.2.5 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s' % (7, 'January'))

# 24.2.6 format 메서드 사용하기
print('Hello, {}'.format('world!'))
print('Hello, {0}'.format('world!'))

# 24.2.7 format 메서드로 값을 여러 개 넣기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.8))

# 24.2.8 format 메서드로 같은 값을 여러 개 넣기
print('{0} {1} {0} {1}'.format('Python', 'Script'))

# 24.2.9 format 메서드에서 인덱스 생략하기
# 만약 {}에서 인덱스를 생략하면 format에 지정한 순서대로 값이 들어간다.
print('Hello, {} {} {}'.format('Python', 'Script', 3.8))

# 24.2.10 format 메서드에서 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language='Python', version=3.8))

# 24.2.11 문자열 포매팅에 변수를 그대로 사용하기 (f-string)
language = 'Python'
version = 3.6
print(f'f-string : Hello, {language} {version}')

# 24.4 연습문제 : 파일 경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path[path.rfind('\\')+1:]
print(filename)

# 24.5 심사문제 : 특정 단어 개수 세기
input_list = input().split(' ')
for i, v in enumerate(input_list):
    input_list[i] = v.strip('.,')
print(input_list.count('the'))

# 24.6 심사문제 : 높은 가격순으로 출력하기
prices = input().split(';')
prices = list(map(int, prices))
prices.sort(reverse=True)
for price in prices:
    print('{:>9,}'.format(price))
