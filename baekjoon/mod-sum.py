# N개의 수 A1, A2, ..., An
# 연속된 부분의 합이 M으로 나누어떨어지는 구간의 개수
# 1번째 줄 N, M (1<=N<=10^6, 2<=M<=10^3) 2번째 줄 (0<=M<=10^9)

# N, M = map(int,input().split())
# array = list(map(int, input().split()))

N, M = 5, 3
array = [1, 2, 3, 1, 2]
cnt = 0
for i in range(N):
    print(f"i:{i}")
    for d in range(i, N):
        check = 0
        for j in range(i, d+1):
            check += array[j]
        print(f"check:{check}")
        if check % M == 0:
            cnt += 1
    print(f"======")
print(cnt)







