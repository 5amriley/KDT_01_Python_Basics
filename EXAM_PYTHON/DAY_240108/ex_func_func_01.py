# --------------------------------------------------------
# nonlocal 키워드
# --------------------------------------------------------
def print_hello():
    hello='hello~!'

    def print_message():
        msg = hello + ' ^^ '
        print(msg)

    print_message()

# 함수 호출
print_hello()
# print_message()   # 접근 불가
# print(msg)        # 접근 불가

def ff():
    x = 100     # 함수 ff의 지역변수
    def a():
        def b():
            nonlocal x  # 가장 가까운 바깥 함수에서 x를 찾음
            x += 20  # 함수 b의 지역변수
            print(x)
        b()
    a()
ff()
