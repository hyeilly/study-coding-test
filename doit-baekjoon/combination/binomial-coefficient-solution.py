import sys
input = sys.stdin.readline
N, K = map(int, input().split())
D = [[0 for j in range(N + 1)] for i in range(N + 1)]

# 초기화
for i in range(0, N + 1):
    D[i][1] = i # i개에서 1개 선택 경우의 수는 i개
    D[i][0] = 1 # i개에서 1개도 선택하지 않는 경우의 수 1개
    D[i][i] = 1 # i개에서 모두 선택하는 경우의 수 1개

# 점화식으로 D 배열 채우기
for i in range(2, N + 1):
    for j in range(1, i): # N개 중에 K개 뽑을 때 N보다 K 더 클 수 없음.
        # 3개중에 5개를 뽑는 경우의 수는 계산하지 않음
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]
        D[i][j] = D[i][j] % 10007 # 덧셈에 대해서 분배법칙 성립
print(D[N][K])

