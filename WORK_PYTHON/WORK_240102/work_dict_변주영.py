# [Unit 12. 딕셔너리 사용하기]

lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}
print(lux)

# 키가 중복되면
lux = {'health':490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72}
print(lux)

# 빈 딕셔너리 만들기
x = {}
print(x, type(x))

# dict()로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

# dict(), zip()
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

# dict(), 튜플
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

# 딕셔너리의 키에 접근
print(lux['health'])

# 딕셔너리 키에 값 할당하기
lux['health'] = 2037
print(lux)

# 딕셔너리에 키가 있는지 확인하기
print('health' in lux)
print('attack_speed' not in lux)

# 딕셔너리의 키 개수 구하기
print(len(lux))

# 연습문제
camille = {
    'health': 576.6,
    'health_regen' : 1.7,
    'mana' : 338.8,
    'mana_regen' : 1.63,
    'melee' : 125,
    'attack_damage' : 60,
    'attack_speed' : 0.625,
    'armor' : 26,
    'magic_resistance' : 32.1,
    'movement_speed' : 340
}

print(camille['health'])
print(camille['movement_speed'])

# 심사문제
key_list = input().split()
value_list = input().split()
input_dict = dict()
for i in range(len(key_list)):
    input_dict[key_list[i]] = value_list[i]
print(input_dict)

