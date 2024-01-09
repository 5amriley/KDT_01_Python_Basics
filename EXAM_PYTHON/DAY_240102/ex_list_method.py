# ---------------------------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법 : 데이터.메서드명() 또는 변수명.메서드명()
# -----------------------------------------------------------------------
# List 전용 메서드 살펴보기
# [1] 리스트에 데이터를 추가하는 메서드 => append() 맨 끝에 원소로 추가
nums = []
print(f'len(nums) : {len(nums)}')

nums.append(88)
nums.append('손에 손잡고')
print(nums)

# [2] 리스트에 데이터를 추가하는 메서드 => insert(위치인덱스, 데이터) => 지정 위치에 추가
nums.insert(0, 2024)
print(nums)

nums.insert(-1, ["ABC", "DEF"])
print(nums)

# 'DEF' 데이터 삭제
del nums[-2][1]
print(nums)

# 리스트 안 모든 원소 삭제해서 빈 리스트를 만들어주세요
del nums[:]
print(f'len(nums) : {len(nums)}개, {nums}')

# 리스트 안의 원소 / 요소를 정렬해주는 메서드 => sort() 오름차순 정렬
# - 오름차순 : 작은 수 >>> 큰 수
nums.append(5)
nums.append(1)
nums.append(0)
nums.append(7)
nums.append(9)

nums.sort()
print(nums)

# 내림차순 : 큰 수 >>> 작은 수
nums.sort(reverse=True)
print(nums)

# [3] 리스트 안의 원소 / 요소의 현재 위치를 반대로 뒤집어 주는 메서드 => reverse()
# 원소 / 요소 데이터 값 비교 안 함!! 순서만 변경함!
nums.reverse()
print(f'nums : {len(nums)}개, {nums}')

# [4] 리스트 안의 원소 / 요소를 삭제해주는 메서드 => remove(데이터)
# - 리스트에서 지정된 값 삭제 (처음 나오는 값 1개 삭제)
# - 없는 값/데이터 요청 시 Error 발생시킴!!!
nums.remove(0)
print(f'nums : {len(nums)}개, {nums}')

# [5] 리스트 안의 모든 원소/요소를 삭제해주는 메서드 => clear()
nums.clear()
print(f'nums : {len(nums)}개, {nums}')

# [6] 리스트의 원소/요소를 꺼내는 메서드 => pop()
nums.append(-10)
nums.append(0.01)
nums.append(3)

# 제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop()
print(f'nums : {len(nums)}개, {nums}')

# 특정 위치의 원소/요소 데이터 꺼내기 => pop(인덱스)
nums.pop(0)
print(f'nums : {len(nums)}개, {nums}')

# [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 카운팅해주는 메서드 => count(데이터)
print(nums.count('A'))
print(nums.count(0.01))

# [8] 리스트를 확장시키는 메서드 => extned(), 파괴적 (리턴값 None)
nums.extend([11, 22, 33])
print(f'nums : {len(nums)}개, {nums}')

nums.extend("새해 복 많이 받으세요")
print(f'nums : {len(nums)}개, {nums}')

nums.extend(["새해 복 많이 받으세요"])
print(f'nums : {len(nums)}개, {nums}')

# nums.extend(2024) # iterable 이 아니므로 오류 발생
print(f'nums : {len(nums)}개, {nums}')

# [9] 리스트를 얕게 복사해주는 메서드 => copy()
nums.append([100, 200])

nums2 = nums.copy()
print(nums2)
print(id(nums))
print(id(nums2))

nums[-2] = 2024
print(nums)
print(nums2)

# 리스트의 경우 힙에서 주소가 저장되어 그 주소를 참조하는 데이터형 (한 단계 더 거침)
# copy시 리스트는 주소만 복사되기 때문에 copy본도 똑같은 리스트 데이터를 참조한다.
nums[-1][0] = 77
print(nums)
print(nums2)
