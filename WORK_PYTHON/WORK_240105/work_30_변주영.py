# [Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기]

DEBUG = int(input("실행하려는 문제의 번호를 입력하세요 : "))    # 1: 연습문제, 2: 심사문제

DEBUG_E1 = False
if DEBUG_E1:
    # 30.1.1 위치 인수를 사용하는 함수를 만들고 호출하기
    def print_numbers(a, b, c):
        print(a)
        print(b)
        print(c)


    # 30.1.2 언패킹 사용하기
    x = [10, 20, 30]

    print_numbers(*x)
    print_numbers(*[100, 200, 300])

    # print_numbers(*[10, 20])

DEBUG_E2 = False
if DEBUG_E2:
    # 30.1.3 가변 인수 함수 만들기
    def print_numbers(*args):
        for arg in args:
            print(arg)


    print_numbers(10, 20, 30, 40)
    print_numbers(10)

    x = [100]
    print_numbers(*x)

    y = [2, 4, 6, 8]
    print_numbers(*y)


    def print_numbers2(a, *args):
        print(a)
        print(args)


    print_numbers2(1)
    print_numbers2(1, 17, 19)
    print_numbers2(*[5, 6, 7])

DEBUG_E3 = False
if DEBUG_E3:
    # 30.2 키워드 인수 사용하기
    def personal_info(name, age, address):
        print('이름: ', name)
        print('나이: ', age)
        print('주소: ', address)


    personal_info('홍길동1', 30, '서울시 용산구 이촌동')
    personal_info(30, '홍길동2', '서울시 용산구 이촌동')
    personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동3')

    # 30.3 키워드 인수와 딕셔너리 언패킹 사용하기
    x = {'name':'김길동', 'age':10, 'address':'강원도 속초시'}
    personal_info(**x)

    personal_info(**{'name':'박길동', 'age':15, 'address':'경기도 고양시'})
    # personal_info(**{'name':'이길동', 'old':15, 'address':'경기도 고양시'})

    # 30.3.1 **를 두 번 사용하는 이유
    y = {'age1': 10, 'name1': '김길동', 'address1': '강원도 속초시'}
    personal_info(*y)   # 딕셔너리에 * 한 개만 사용하여 언패킹 => 키가 언패킹된다.
    # personal_info(**y)

    def personal_info2(**kwargs):
        # kwargs 안에 특정 키가 있는지 먼저 확인한다.
        if 'name' in kwargs:
            print('이름: ', kwargs['name'])
        if 'age' in kwargs:
            print('나이: ', kwargs['age'])
        if 'address' in kwargs:
            print('주소: ', kwargs['address'])

    personal_info2(name='마길동', age='25', where='대전시 동구')

DEBUG_E4 = False
if DEBUG_E4:
    # 30.4 매개변수에 초기값 지정하기
    def personal_info(name, age, address='비공개'):
        print('이름: ', name)
        print('나이: ', age)
        print('주소: ', address)


    personal_info(name='번길동', age=35)  # address 생략
    personal_info(age=1, address='경상북도 울릉군', name='가길동')

if DEBUG == 1:
    # 연습문제
    korean, english, mathematics, science = 100, 86, 81, 91


    def get_max_score(*args):
        return max(args)


    max_score = get_max_score(korean, english, mathematics, science)
    print('높은 점수: ', max_score)
    max_score = get_max_score(english, science)
    print('높은 점수: ', max_score)


if DEBUG == 2:
    # 심사문제
    korean, english, mathematics, science = map(int, input().split())

    def get_min_max_score(*args):
        return min(args), max(args)

    def get_average(korean=-1, english=-1, mathematics=-1, science=-1):
        total = 0
        cnt = 0
        if korean >= 0: total += korean; cnt += 1
        if english >= 0: total += english; cnt += 1
        if mathematics >= 0: total += mathematics; cnt += 1
        if science >= 0: total += science; cnt += 1

        if cnt == 0:
            return -1
        else:
            return total / cnt

    min_score, max_score = get_min_max_score(korean, english, mathematics, science)
    average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
    print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

    min_score, max_score = get_min_max_score(english, science)
    average_score = get_average(english=english, science=science)
    print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
