# ---------------------------------------------------------
# str 데이터 타입과 관련된 내장함수
# ---------------------------------------------------------
# 원소/요소의 갯수를 알려주는 내장함수 => length 의 약자 len()
msg = "christmas2023!"

print(f'len(msg) = {len(msg)}')
# print(f'len(2024) = {len(2024)}') # 숫자 데이터는 길이, 즉 요소가 없다.

# 문자의 코드값을 알려주는 내장함수 => ord(문자1개)
print(ord('a'))
print(ord('!'))

# Hello의 코드값 출력하기
code_H = ord('H')
code_e = ord('E')
code_l = ord('l')
code_o = ord('o')

print(f'Hello의 코드값 => {code_H} {code_e} {code_e} {code_l} {code_o}')
print(f'Hello의 이진수값 => {bin(code_H)} {bin(code_e)} {bin(code_e)} {bin(code_l)} {bin(code_o)}')
print(f'Hello의 이진수값 => {bin(code_H)[2:]} {bin(code_e)[2:]} {bin(code_e)[2:]} {bin(code_l)[2:]} {bin(code_o)[2:]}')


# 코드값에 해당하는 문자를 반환해주는 내장 함수 => character 의 약자 chr()
# 코드값 65에 해당하는 문자 반환
print(f'chr(65) = {chr(65)}')

'''
사람문자 -> 기계어 : 인코딩 (Encoding) ~~~ ord(사람문자1개)
기계어 -> 사람문자 : 디코딩 (Decoding) ~~~ chr(코드1개)
'''
