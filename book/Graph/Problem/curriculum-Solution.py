from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    # 첫 번째 수는 시간 정보를 담고 있음
    time[i] = data[0]
    print(f"data:{data}")
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)
        print(f"x:{x}")
        print(f"update graph: {graph}")
print(f"time:{time}")
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(time)
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        print(f"graph:{graph}")
        for i in graph[now]:
            print(f"now:{now}")
            print(f"time:{time}")
            print(f"result:{result}")
            result[i] = max(result[i], result[now] + time[i])
            print(f"result[now]:{result[now]}")
            print(f"time:{time[i]}")
            print(f"result[i]:{result[i]}")
            print(f"time:{time}")
            print(f"result:{result}")
            print()
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])
topology_sort()