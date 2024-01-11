n, k = 3, 7
array = [2, 3, 5]
# n, k = 3, 4
# array = [3, 5, 7]

# 15원을 만들기 위해 3원을 5개 사용
# 1<=N<=100, 1<=M<=10000
# 비효율적인 것 부터 계산
d = [10001] * (k + 1)
i = 2
d[0] = 0
print(d)
for i in array:
    for j in range(i, k+1):
        if d[j - i] != 10001:
            d[j] = min(d[j - i] + 1, d[j])


if d[k] > 10000:
    print(-1)
else:
    print(d[k])

    # for j in range(i, len(d)):
    #     if j % 2 == 0:
    #         print(j)
    # if i % 2 == 0:
    #     d[i]= i // 2
    # if i % 3 == 0:
    #     print(f"i:{i} d[i]:{d[i]}")
print(d)
