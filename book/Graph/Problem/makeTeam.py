# 서로소 집합 찾기의 경우
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = []
for i in range(N + 1):
    parent.append(i)
print(parent)
for _ in range(M):
    u, a, b = map(int, input().split())
    if u == 0:
        union_parent(parent, a, b)
    elif u == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
