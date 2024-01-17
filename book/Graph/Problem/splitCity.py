def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

N, M = map(int, input().split())
parent = []
for i in range(N + 1):
    parent.append(i)
print(parent)
edges = []
for e in range(M):
    cost, a, b = map(int, input().split())
    edges.append((cost, a, b))
# 낮은비용부터 sort
edges.sort()
print(edges)
result, last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
    print(result - last)
    print(edge)