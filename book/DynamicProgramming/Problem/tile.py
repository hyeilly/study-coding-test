# 가로 길이 N, 세로 길이 2
# 얇은 바닥 1x2 덮개, 2x1 덮개, 2x2 덮개
# 사용할 수 있는 덮개의 형태는 2x2 직사각형
# 1<=N<=1000

# 왼쪽부터 N - 2 까지 길이가 덮개로 이미 채워져 있는 경우 덮개를 채우는 방법
# Ai = Ai-1 +Ai-2 + Ai-2 => Ai = Ai-1 + Ai-2 * 2

n = 3

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])