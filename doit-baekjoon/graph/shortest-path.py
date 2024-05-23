# 에지의 가중치 10이하의 자연수인 방향 그래프 = 자연수 = 양수 에지
# 시작점에서 다른 모든 노드로의 최단 경로

N, E = 5, 6 # 노드 개수, 에지 개수
S = 1 # 출발 노드

graph = [
    [5, 1, 1],
    [1, 2, 2],
    [1, 3, 3],
    [2, 3, 4],
    [2, 4, 5],
    [3, 4, 6]
]
# 인접리스트 노드 저장
graph_dic = {}
for g in graph:
    start = g[0]
    end = g[1]
    edge = g[2]
    if start not in graph_dic:
        graph_array = []
    graph_array.append([end, edge])
    graph_dic[start] = graph_array
    graph_array.sort(key=lambda x:x[0])
print(graph_dic)

result = [float('inf') for _ in range(E)]
# 출발노드는 0으로 초기화
result[S - 1] = 0
print(result)
# 우선순위 큐에 먼저 삽입

pr = []
for (rdx, r) in enumerate(result):
    if r == 0:
        node = rdx + 1
        pr.append(node)
        print(pr)
        for (gdx, g) in enumerate(graph_dic[node]):
            print(g)
            target = g[0]
            compB = result[target - 1]
            compA = result[rdx] + g[1]
            if compA < compB:
                result[target - 1] = compA
            else:
                result[target - 1] = compB
            print(result)







