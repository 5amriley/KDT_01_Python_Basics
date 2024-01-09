'''
논리 연산자 -> and, or, not
- 결과 : True, False
- 동작방식
    * and => A and B : A, B 모두 True일 때만 True
    * or => A or B : A, B 중 하나 이상 True라면 True
    * not => not A : 현재 A의 상태를 반대로 (토글링), not True -> False
'''

no1, no2 = 10, 3

# and 연산자 ------------------------------------------------------
print(no1>no2, no1>100)
print(no1>no2 and no1>100)
print(no1>no2 and no1>100 and no2>0)

# or 연산자 -------------------------------------------------------
print(no1>no2, no1>100)
print(no1>no2 or no1>100)
print(no1>no2 or no1>100 or no2>0)

# not 연산자 ------------------------------------------------------
# False => 0, True => 1 [0이 아닌 모든 숫자]
print(not False, not True)
print(not 0, not 1)
print(not 2)
print(not 2, not -3, not 0.0)

'''
객체 비교 연산자 => is, is not
- 결과 : True, False
- 동작 방식
    * is => A is B : A, B가 동일한 데이터 타입의 객체 여부
    * is not => A is not B : A, B가 서로 다른 데이터 타입의 객체 여부
[주의] >, <, >=, <=, ==, != 는 '값'을 비교하는 연산자! (수치비교)
'''

print(f'10 is 10 -> {10 is 10}')
print(f'10 is 10 -> {10 is 10.0}')

print(f'10 == 10 -> {10 == 10}')
print(f'10 == 10.0 -> {10 == 10.0}')

# --------------------------------------------------------------------
# [실습1] 2게 슷지 데이터를 입력받은 후 2개의 값을 산술 연산한 값을 결과로 출력해 주세요.
#        +, -, *, /, //, %, **
#        [출력 예시] 10 + 4 = 14
# ---------------------------------------------------------------------

num1 = int(input("첫 번째 정수 입력 : "))
num2 = int(input("두 번째 정수 입력 : "))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

# --------------------------------------------------------------------
# [실습2] [실습1]에서 입력받은 숫자 데이터를 활용하여 비교 연산한 결과를 출력하세요.
#        >, <, >=, <=, ==, !=
#        [출력 예시] 10==4 -> False
# --------------------------------------------------------------------

print(f'{num1} > {num2} -> {num1 > num2}')
print(f'{num1} < {num2} -> {num1 < num2}')
print(f'{num1} >= {num2} -> {num1 >= num2}')
print(f'{num1} <= {num2} -> {num1 <= num2}')
print(f'{num1} == {num2} -> {num1 == num2}')
print(f'{num1} != {num2} -> {num1 != num2}')

# --------------------------------------------------------------------
# [실습3] [실습1]에서 입력받은 숫자 데이터를 활용하여
#        최대값과 최소값을 추가로 입력받은 후 논리연산한 결과 값을 출력하세요.
#        [출력 예시] 10>4 and 10>최대값   -> True
#                  10>4 and 10>최소값   -> True
#                  not 10              -> False
# --------------------------------------------------------------------

max_num = int(input("최대값을 입력하세요 : "))
min_num = int(input("최소값을 입력하세요 : "))

print(f'{num1}>{num2} and {num1}>{max_num} -> {num1>num2 and num1>max_num}')
print(f'{num1}>{num2} and {num1}>{min_num} -> {num1>num2 and num1>min_num}')
print(f'{num1}<{num2} or {num2}>{max_num} -> {num1<num2 or num2>max_num}')
print(f'{num1}<{num2} or {num2}>{min_num} -> {num1<num2 or num2>min_num}')
print(f'not {num1} -> {not num1}')
print(f'not {num2} -> {not num2}')
