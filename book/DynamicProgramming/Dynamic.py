def make1():
    x = 26
    d = [0] * 30001
    for i in range(2, x+1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    print(d[x])

def antdie():
    n = 4
    d = [0] * 1001
    array = [1, 3, 1, 5]
    d[0] = array[0]
    d[1] = max(array[1], array[0])
    # [1, 3, 0, 0]
    for i in range(2, n):
        d[i] = max(d[i-1], d[i - 2] + array[i])
        print(i)
    print(d[n-1])

def tile():
    n = 3
    d = [0] * 1001
    # 타일 1개일때 경우의 수 2 x 1
    d[1] =  1
    # 타일 2개일 때 경우의 수 1 x2 2개 / 2 x 1 2개 / 2 x 2 1개
    d[2] = 3
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + (d[i - 2] * 2)) % 796796
    print(d[n])

# make1()
# antdie()
tile()