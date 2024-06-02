# 1번째 줄에 노드의 개수 N,
# N - 1개 줄에는 트리상에서 연결된 두 노드
# M은 가장 가까운 공통 조상을 알고싶은 쌍의 개수
# M개의 줄에는 노드의 쌍이 주어짐
# 정답 2 4 2 1 3 1

from collections import deque

N = 15
tree = [
    [1, 2], [1, 3], [2, 4], [3, 7], [6, 2], [3, 8], [4, 9], [2, 5], [5, 11], [7, 13], [10, 4], [11, 15], [12, 5], [14, 7]
]
M = 6
q = [[6, 11], [10, 9], [2, 6], [7, 6], [8, 13], [8, 15]]
list = [[] for i in range(N+1)]
depth = [0 for i in range(N+1)]
visited = [0 for i in range(N+1)]
parent = [[0] * 21 for _ in range(10001)]

# 1 인접리스트로 트리 데이터 구현
for t in tree:
    first, second = t
    list[first].append(second)
    list[second].append(first)

def BFS(node):
    queue = deque([node])
    visited[node] = True
    level = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in list[now_node]:
            if visited[next] == False:
                visited[next] = True
                queue.append(next)
                parent[0][next] = now_node
                depth[next] = level
        count += 1
        if(count == now_size):
            count = 0
            now_size = len(queue)
            level += 1
        print(queue)

def executeLCA(a, b):
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp
    for k in range(kmax, -1, -1):
        if 2**k <= depth[b] - depth[a]:
            b = parent[k][b]
    for k in range(kmax, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    LCA = a
    if a != b:
        LCA = parent[0][LCA]
    return LCA


temp = 1
kmax = 0
while(temp <= N):
    temp *= 2
    if (temp > N):
        break
    kmax += 1
print(kmax)
BFS(1)

for k in range(1, kmax+1):
    for n in range(1, N +1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]

for i in q:
    a, b = i
    print(executeLCA(a, b))