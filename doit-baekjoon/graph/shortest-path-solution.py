# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

import sys

input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V + 1)]
q = PriorityQueue()

# 인접리스트
# 에지 개수만큼 반복
for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v, w)) # 도착노드, 가중치

# 앞에 0먼저 쓴 이유는 우선순위 큐 쓸 때 앞에 있는거 기준으로 정렬
# 현재 노드의 거리배열 리스트
q.put((0, K))
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for temp in myList[c_v]:
        next = temp[0]
        value = temp[1]
        if distance[next] > (distance[c_v] + value):
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")