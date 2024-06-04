# 정수를 1으로 만들기 (백준 1463)
# 바텀-업 방식
# 정수 X에 사용할 수 있는 연산 3가지
# 1 X가 3으로 나누어 떨어지면 3으로 나눔
# 2 X가 2로 나누어 떨어지면 2로 나눔
# 3 1을 뺀다
# 적절히 사용해 1을 만들고, 연산을 사용하는 횟수의 최솟값 출력
# 입력 : N  ex)10
# 출력 : 최솟값 ex)3

# D[10] 은 10을 1로 만드는데 사용되는 연산의 최솟값

n = int(input())
dp = [-1 for i in range(n + 1)]

# 나누어 떨어지기만 하면
dp[0] = 0
dp[1] = 0 # 1이 1이 될 때 까지 필요한 연산 횟수
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i/2)] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i/3)] + 1)


result = dp[n]
print(result)