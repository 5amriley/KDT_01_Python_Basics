# -----------------------------------------------------
# 참조형 변수 => 데이터 주소 저장
# -----------------------------------------------------
# 저장된 데이터 & 변수 타입 관계 ---------------------------
num = 12
print(f'num => {id(num)}, {type(num)}')

num = 3.
print(f'num => {id(num)}, {type(num)}')

num = 'Good'
print(f'num => {id(num)}, {type(num)}')

num = []
print(f'num => {id(num)}, {type(num)}')

num2 = [11, 22.1]
print(f'num2 => {id(num2)} {type(num2)}')
print(f'num2[0] => {id(num2[0])} {type(num2[0])}')
print(f'num2[1] => {id(num2[1])} {type(num2[1])}')

print("=========== 값 변경 ===============")
# 리스트 원소가 바뀐다고 해서 리스트 자체의 시작주소가 바뀌지는 않는다. (num2)
num2[0] = 100
print(f'num2 => {num2} : {id(num2)}, {type(num2)}')
print(f'num2[0] => {num2[0]} : {id(num2[0])}, {type(num2[0])}')

# 리스트를 다른 리스트로 변경
num1 = num2
print(f'num1 => {id(num1)}, {num1}')
print(f'num2 => {id(num2)}, {num2}')

num1[0] = 77
print(f'num1 => {id(num1)}, {num1}')
print(f'num2 => {id(num2)}, {num2}')