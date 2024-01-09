# ---------------------------------------------------------
print("[문제 1]")
# ---------------------------------------------------------
address1 = "kim1234@naver.com"
print(address1[:7])

address2 = "http://www.naver.com"
print(address2[11:])

hong = "홍길동"
print(hong[1:])

str1 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
print(str1[::2], str1[1::2])

str2 = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
print(str2[3::4])

social = "881120-1068234"
print(social[:6], social[7:])


# ---------------------------------------------------------
print("[문제 2]")
# ---------------------------------------------------------
num = int(input("정수 입력 : "))

print(f"10진수 : {num}")
print(f"16진수 : {hex(num)}")     # 0x
print(f"8진수 : {oct(num)}")      # 0o
print(f"2진수 : {bin(num)}")      # 0b


# ---------------------------------------------------------
print("[문제 3]")
# ---------------------------------------------------------
word1 = input("첫번째 단어 입력 : ")
word2 = input("두번째 단어 입력 : ")
word3 = input("세번째 단어 입력 : ")

print(f'코드 값이 가장  큰 단어 : {max(word1, word2, word3)}')
print(f'코드 값이 가장 작은 단어 : {min(word1, word2, word3)}')


# ---------------------------------------------------------
print("[문제 4]")
# ---------------------------------------------------------
the_message = "데이터"
q4_input = input("단어 입력 : ")
print(f"'{the_message}' 단어 메시지 존재 여부 : {the_message in q4_input}")


# ---------------------------------------------------------
print("[문제 5]")
# ---------------------------------------------------------
q5_input = input("단어 입력 : ")
code_z = ord(q5_input[0])
code_o = ord(q5_input[1])
# (1) 문자 1개에 대한 코드값 => ord('문자1개')
# (2) 원하는 진수로 변환 => bin(10진수 코드값), hex(10진수 코드값)
print(f"'{q5_input}' 코드값 : {code_z} {code_o} {code_o}")
print(f"'{q5_input}' 16진수 코드값 : {bin(code_z)} {bin(code_o)[2:]} {bin(code_o)[2:]}")
