def find_num():
    N = int(input())
    list = list(map(int, input().split()))
    find = int(input())
    cnt = 0
    for l in list:
        if find == l: cnt += 1
    print(cnt)

def print_num():
    N, X = map(int, input().split())
    list = list(map(int, input().split()))
    for l in list:
        if l < X:
            print(l, end=' ')

def min_max():
    N = int(input())
    list = list(map(int, input().split()))
    print(min(list), max(list))

list = []
for _ in range(9):
    N = int(input())
    list.append(N)
print(max(list), list.index(max(list)) + 1)