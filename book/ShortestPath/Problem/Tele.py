import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
# 연결 그래프 저장공간
graph = [[] for i in range(N + 1)]
# 짧은 거리를 담을 수 있는 리스트
distance = [INF] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    # X 노드에서 다른 Y 노드 로 이어지는 메시지 Z
    graph[X].append((Y, Z))
print(graph)

def dijkstra(start):
    q = []
    # q에 push 할 것임. 최단 경로 0, 시작노드
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # (0, 1) => 1번 노드의 거리는 0
        dist, now = heapq.heappop(q)
        # 위에서 push 할때 이미 간 곳이므로 0지정했음
        if distance[now] < dist:
            continue
        # 현재 그래프에 있는 노드와 간선을 계산해서 최소 거리를 구해야함
        for i in graph[now]:
            cost = i[1] + dist # 현재 거리와 거리 계산하기
            if cost < distance[i[0]]:
                # 거리가 더 짧은 것이므로 업데이트
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(C)

count = 0
max_result = 0
print(distance)
for i in distance:
    if i != INF:
        count += 1
        max_result = max(i, max_result)
print(count - 1, max_result)



