# 최소 신장 트리 정답

import sys
from queue import PriorityQueue
input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))  # 가중치 기준으로 정렬하므로

# 자신의 부모노드 찾기
def find(a):
    if(a == parent[a]):
        return a
    else:
        # return find(parent[a]) 이것도 가능하지만
        # union find에서 경로압축을 하기 위해
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    # 각각 부모노드
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a # 부모노드로

useEdge = 0
result = 0

while useEdge < N - 1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)