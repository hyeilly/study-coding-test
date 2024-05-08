# 입력
# 2차원 배열의 크기, 구간 합 질의의 개수
# 원본 배열 1번째줄
# 원본 배열 2번째줄
# 원본 배열 3번째줄
# 원본 배열 4번째줄
# 구간 합 (X1, Y1), (X2, Y2) 1번째 질의
# 구간 합 (X1, Y1), (X2, Y2) 2번째 질의
# 구간 합 (X1, Y1), (X2, Y2) 3번째 질의
# 조건 1 <= N <=1024, 1<=M<=100,000

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)