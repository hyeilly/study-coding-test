# 최악의 경우에도 시간복잡도 O(ElogV) 보장해 해결
# 힙 자료구조
#  - 특정 노드까지의 최단 거리에 대한 정보 담아서 처리
#  - 출발노드로부터 가장 거리가 짧은 노드를 빠르게 찾을 수 있음
from collections import deque

graph = {
    1: [(2, 2), (3, 5), (4, 1)],
    2: [(3, 3), (4, 2)],
    3: [(2,3), (6, 5)],
    4: [(3,3), (5, 1)],
    5: [(6,2), (3,1)],
    6: [()]
}

# step0
queue = deque()
# 1번 노드 출발
# 모든 노드의 최단 거리를 무한으로 설정
distance = [int(1e9)] * len(graph)
distance[0] = 0
queue.append((0, 1))
# print(distance)
# 가장 짧은 노드를 선택하기 위해서 우선순위 큐에서 그냥 노드를 꺼내기
# 우선순위 큐에서 노드를 꺼낸 뒤
# 해당 노드를 이미 처리한 적이 있다면 무시
# 아직 처리하지 않은 노드에 대해서만 처리

# step1
# 1번 노드까지 가는 최단 거리가 0
# 1번 노드를 거쳐서 2, 3, 4번 노드로 가는 최소 비용 계산
node = queue[0][1]
queue.remove(queue[0])
# 거리가 가까운거 순서로 정렬
graph[node].sort(key=lambda x: x[1])
# print(graph[node])
# print(distance)
for i in graph[node]:
    key = i[0]
    value = i[1]
    # print(key, value)
    distance[key - 1] = value
    # 튜플 순서 (노드, 거리)
    queue.append((key, value))
# print(queue)
# print(distance)

# step2
print(queue[0])
# node 4 를 꺼내기
# 4와 연결된 간선 찾기
node = queue[0][0]
print(graph[node])

queue.remove(queue[0])
print(queue)

