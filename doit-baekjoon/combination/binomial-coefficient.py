# 조합 - 이항계수 구하기2
# 자연수 N과 정수 K가 주어졌을 때 이항계수를 10,007로 나눈 나머지 구하는 프로그램
# nCk => n개 중에 k개를 뽑는 경우의 수
# 1<=N<=1,000 / 0 <=K <= N 변수 표현 범위를 넘어감
# 나머지 MOD 연산의 분배법칙에 대해 알고있는지

N = 5
K = 2

# Mod
# (A mod N + B mod N) mod N = (A + B) mod N
# 덧셈 연산 시 한번 process 할때마다 mod 연산 필요

# 5C2
# dp = [[0 for _ in range(N + 1)]] * (N + 1)
dp = [[0 for _ in range(N +1)] for _ in range(N + 1)]

# 초기화
for i in range(N + 1):
    dp[i][1] = i
    dp[i][0] = 1
    dp[i][i] = 1

# D[5][2] = D[4][2] + D[4][1]
for i in range(N + 1):
    for j in range(i + 1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        dp[i][j] %= 10007
print(dp)
result = dp[N][K - 1]
print(result)