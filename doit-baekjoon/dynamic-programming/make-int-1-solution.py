import sys
# input 재정의하지 않으면 데이터 입력받는 시간이 느림
input = sys.stdin.readline

N = int(input())
D = [0] * (N + 1)
# 초기화
D[1] = 0 # 1이 되기 위해 필요한 최소 연산 횟수 이므로

for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)

print(D[N])


