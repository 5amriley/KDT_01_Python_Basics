# ------------------------------------------------------------------------
# [실습1] 2개의 정수를 입력받은 후 사칙연산 수행결과를 반환하는 기능의 함수를 정의하세요
#        함수이름 : fourCalc
#        매개변수 : n1, n2
#        반환결과 : 사칙연산 결과
# ------------------------------------------------------------------------
def fourCalc(num1, num2):
    result = []
    result.append(num1 + num2)
    result.append(num1 - num2)
    result.append(num1 * num2)
    if not num2:
        result.append('0으로 나눌 수 없음')
    return result

# -------------------------------------------------------------------------
# [실습2] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해 주세요
#        문자열 ---> 코드값 ---> 16진수 코드값
#        함수이름 : getCode
#        매개변수 : message
#        변환결과 : str
# -------------------------------------------------------------------------
def getCode(message):
    result = []
    for char in message:
         result.append(hex(ord(char)) + ' ')
    return ''.join(result)

print(fourCalc(10, 0))
print(getCode('hello'))
