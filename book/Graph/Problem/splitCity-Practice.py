# 마을은 N개의 집, M개의 길로 이루어짐
# 어느 방향으로든지 다닐 수 있음
# 2개의 분리된 마을로 분할할 계획
# 마을 안에 있는 임의의 두 집 사이 경로가 항상 존재해야함
# N은 2이상 100,000이하 정수, M은 1이상 1,000,000이하인 정수
# M 줄에 걸쳐 길의 정보 A, B, C 3개의 정수 공백
# A번 집 부터 B번 집까지 연결하는 유지 비 C
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
# 크루스칼 알고리즘으로 최소 신장 트리 찾기 => 간선 중 가장 비용 큰 간선 제거
N, M = 7, 12
parent = []
for i in range(N + 1):
    parent.append(i)
print(parent)
A, B, C = 1, 2, 3
edges = []
result = 0

# 1부터 2까지 걸린 거리 3
edges.append((C, A, B))
print(edges)
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)