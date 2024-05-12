# 오큰수 구하기
# 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수 의미
# A = [3, 5, 2, 7]
M = int(input())
A = list(map(int, input().split()))
# M = 4
# A = [3, 5, 2, 7]

answer = []
for (adx, a) in enumerate(A):
    check = A[adx+1:]

    if len(check) > 0:
        for c in check:
            if a < c:
                answer.append(str(c))
                break
    else:
        answer.append(str(-1))
print(' '.join(answer))