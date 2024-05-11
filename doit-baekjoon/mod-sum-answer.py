# 시간 복잡도를 줄여야함
# 아이디어1)
# (A + B) % C = ((A % C) + (B % C)) % C
# 각각 나머지 연산을 더해 나머지 연산을 한 값
# 아이디어2)
# 구간 합 배열을 이용한 식 S[i] - S[j] = 원본 리스트의 1부터 i까지의 구간 합

# 합 배열 S 생성
# M으로 모두 나머지 연산
# 0 인 것은 다 횟수 더하면 됨
# 나랑 값이 똑같은 것 찾기
#
# N, M = 5, 3
# array = [1, 2, 3, 1, 2]
#
# array_sum = []
# for i in range(N):
#     check = 0
#     for j in range(i+1):
#         check += array[j]
#     array_sum.append(check)
#
# array_sum = [i % M for i in array_sum]
# print(array_sum)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m

answer = 0
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    reminder = S[i] % m
    if reminder == 0:
        answer += 1
    C[reminder] += 1

# 조합 구하는 공식
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)
print(answer)