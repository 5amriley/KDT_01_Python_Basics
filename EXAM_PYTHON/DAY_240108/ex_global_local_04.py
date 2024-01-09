# --------------------------------------------------------
# 주의! 꼭 전역변수가 아니더라도 list, tuple, set, dict의 경우
# 함수의 매개변수로 전달 후 원소값 변경 시 모두 적용됨!
# ==> 해결법 : 깊은 복사 deepcopy 로 복사본 전달 필요!
# --------------------------------------------------------
def one(number):
    print(number)

def datas(nums, value):
    # nums : 리스트
    # value : 정수
    nums[-1] = 1004
    print(nums, value, sep=' - ')

# 전역변수 선언 --------------------------------------------
value = 'Good'
dataList = [11, 22, 33]
num = 7

# 함수 호출
one(num)
datas(dataList, value)

print(f'전역변수값 => value : {value}, dataList : {dataList}, num : {num}')

def foo():
    x = 20
    print(locals())

foo()