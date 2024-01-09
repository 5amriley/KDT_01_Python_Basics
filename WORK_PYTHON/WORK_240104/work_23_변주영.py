# [Unit 23. 2차원 리스트 사용하기]

# 연습문제: 3차원 리스트 만들기
a = [[[0 for c in range(3)] for r in range(4)] for h in range(2)]
print(a)

# 심사문제: 지뢰찾기
col, row = map(int, input().split())
matrix = []
for i in range(row):
    altered_list = list(input().replace('*', '1').replace('.', '0'))
    matrix.append(list(map(int, altered_list)))
print()

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y]:
            print('*', end='')
        else:
            # matrix[x][y] 기준, 주변에 지뢰가 존재할 수 없는 곳 정보 (0 초과 : 지뢰가 존재할 수 없는 곳)
            temp = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # matrix[x][y] 자기자신은 지뢰가 없으므로 1 처리

            # [x0: x 첫줄] [xl: x 마지막줄] [y0: y 첫줄] [yl: y 마지막줄]
            x0, xl, y0, yl = False, False, False, False
            if x == 0: x0 = True
            if x == len(matrix) - 1: xl = True
            if y == 0: y0 = True
            if y == len(matrix[0]) - 1: yl = True

            if x0:
                for i in range(3):
                    temp[0][i] += 1
            if xl:
                for i in range(3):
                    temp[2][i] += 1
            if y0:
                for i in range(3):
                    temp[i][0] += 1
            if yl:
                for i in range(3):
                    temp[i][2] += 1

            result = 0
            for i in range(3):
                for j in range(3):
                    if not temp[i][j]:
                        result += matrix[x+i-1][y+j-1]

            print(result, end='')
    print()
