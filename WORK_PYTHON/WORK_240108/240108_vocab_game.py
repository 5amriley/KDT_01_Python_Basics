# ------------------------------------------------------------
# 영단어 학습앱 (by 변주영 on 2024/01/08)
# 1. 문제 풀기
# 2. 단어 출력
# 3. 단어 추가 (스펠링, 뜻)
# 4. 단어 뜻 수정
# 5. 단어 삭제
# 6. 프로그램 종료
# -------------------------------------------------------------

import random

# 단어 저장할 전역변수 선언 (초기값 : 단어 24개)
words_dict = {'bump':'(~에 신체 부위를) 찧다, 부딪치다', 'conviction':'유죄선고',
              'algorithm':'알고리즘', 'exercise':'(권리 등을) 행사하다, 발휘하다',
              'cram':'벼락치기 공부를 하다', 'reciprocal':'상호간의',
              'delegate':'대표자', 'lucrative':'수익성이 좋은',
              'sidewalk':'보도, 인도', 'permanent':'영구적인, 영원한',
              'nourish':'영양분을 공급하다', 'thesis':'논지',
              'legitimate':'정당한, 타당한', 'conscience':'양심',
              'tuition':'(특히 대학의)등록금', 'parenthesis':'소괄호()기호',
              'reimburse':'배상하다', 'remedy':'바로잡다, 교정하다',
              'novice':'초보자', 'mischievous':'짖궂은, 말썽꾸러기의',
              'rehearsal':'리허설', 'mayonnaise':'마요네즈',
              'canoe':'카누', 'etiquette':'에티켓'
              }

def word_game():
    if len(words_dict) == 0:
        print('저장된 단어가 없어서 플레이할 수 없습니다. 단어를 추가해주세요.')
        return
    else:
        print('\n'*30)  # 위에 단어를 출력했을 경우 안 보이게 밀어버리는 조치
        while True:
            print(f'저장된 단어는 총 {len(words_dict)} 개 입니다.')
            q_input = input('풀고 싶은 문제의 개수를 입력하세요 : ')
            if q_input.isdecimal() and int(q_input)>0:
                break
            else:
                print('잘못된 입력입니다. 다시 입력하세요.')

        qnum = min(len(words_dict), int(q_input))  # 문제 개수 설정
        selected_idx = set()

        while len(selected_idx) < qnum:
            selected_idx.add(random.randint(0, len(words_dict)-1))

        words = words_dict.keys()
        questions = [w for i, w in enumerate(words) if i in selected_idx]
        print(f'총 {qnum}개의 단어가 선택되었습니다.')

        give_up = False
        cnt = 0
        for i, v in enumerate(questions):
            if give_up: break
            print()
            print(f'[{i + 1}번] 단어의 의미 : {words_dict[v]}')
            while not give_up:
                answer = input('단어를 입력하세요 (힌트:1 넘기기:0 종료:-1) : ')
                if answer == '-1':
                    give_up = True
                elif answer == '0':
                    print(f'답은 [ {v} ] 입니다. 아쉽네요 ㅠㅠ')
                    break
                elif answer == '1':
                    print(f'hint : \'{v[0]}\'(으)로 시작하고, 길이는 {len(v)} 예요!')
                elif answer == v:
                    print('정답입니다!')
                    cnt += 1
                    break
                else:
                    print('오답입니다;')
        print()
        if not give_up:
            print('='*54)
            comment = f'[점수] : {cnt} / {qnum} ' + ('[훌륭해요! ^0^]' if cnt / qnum > 0.7 else '[복습할꺼죠? 화이팅!]')
            print(f'{comment:^50}')
            print('='*54)
        print('문제 풀이를 종료합니다.')

def word_display():
    """ 단어 출력 함수 """
    if len(words_dict) == 0:
        print('입력된 단어가 없습니다. 단어를 입력해주세요')
    else:
        print('='*70)
        for key, value in words_dict.items():
            print(f'{key:<35} {value:<35}')
        print('='*70)

def word_add():
    """
    단어 추가 함수\n
    """
    word = None
    cancel = 0  # 중간에 취소했는지 여부
    while True:
        word = input('추가할 단어의 스펠링을 입력해주세요 (입력중지: -1) : ')

        if word == '-1':
            cancel = 1
            break

        if word in words_dict:
            print('이미 추가한 단어입니다.')
            continue
        else:
            meaning = input('단어의 뜻을 입력해주세요 : ')
            words_dict[word] = meaning
            print('입력 완료')
    return cancel

def word_edit():
    """
    단어 수정 함수 (삭제 X) \n
    해당 단어의 맞춘 횟수, 틀린 횟수 유지
    """
    while True:
        word = input('수정할 단어의 스펠링을 입력해주세요 (입력중지: -1) : ')

        if word == '-1': break

        if word not in words_dict.keys():
            print('저장되지 않은 단어입니다.')
            continue
        else:
            meaning = input('단어의 뜻을 입력해주세요 : ')
            words_dict[word] = meaning
            print('수정 완료')
            break

def word_del():
    """ 단어 삭제 함수 """
    global words_dict

    while True:
        target = input('삭제하고 싶은 단어를 입력하세요 (초기화: \'초기화\' 입력, 입력중지: -1): ')
        if target == '초기화':
            words_dict = dict()
            print('초기화 성공!')
            break
        elif target == '-1':
            break
        elif target in words_dict.keys():
            del words_dict[target]
            print('삭제되었습니다.')
        else:
            print('해당하는 단어가 없습니다. 다시 입력하세요.')

word_funcs = [word_game, word_display, word_add, word_edit, word_del]

while True:
    print("[ 주영's 영단어 학습앱 (효과 탁월) ]")
    print("1. 문제 풀기 2. 단어 출력 3. 단어 추가")
    print("4. 단어 뜻 수정 5. 단어 삭제 6. 프로그램 종료")

    choice = input("메뉴 입력 : ")
    if not choice.isdecimal():
        print("잘못된 입력입니다. 다시 입력하세요.\n")
        continue
    elif choice == '6':
        print()
        print('프로그램을 종료합니다.')
        break
    else:
        choice_func = word_funcs[int(choice)-1]
        print()
        choice_func()
        print()
