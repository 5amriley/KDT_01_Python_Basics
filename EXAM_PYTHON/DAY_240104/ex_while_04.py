# ---------------------------------------------------------------
# continue => 계속해서~, 다음 요소/원소
# - 키워드 아래 코드 실행 안 됨
# - 반복 상단으로 이동
# ------------------------------------------------------------------
# 1~30 구성된 리스트 생성하세요
numList = list(range(1, 31))

# 리스트에 요소 중에서 짝수인 경우만 화면에 출력해 주세요
for data in numList:
    if not data % 2:
        print(data)

for data in numList:
    if data % 2:
        continue
    print(data)

# while ===========================================================
idx = 0
while idx < 30:
    if numList[idx] % 2 == 0:
        print(f'{idx}번째 요소 값 : {numList[idx]}')
    idx += 1

idx = 0
while idx < 30:
    if numList[idx] % 2:
        idx += 1
        continue
    print(f'{idx}번째 요소 값 : {numList[idx]}')
    idx += 1
