# 방문하지 않은 노드 중에서 가장 거리가 짧은 노드 매번 선택
# 해당 노드를 거쳐가는 경로 확인해 테이블 갱신
# step1
# 1번 노드를 거쳐갈 때 비용과 현재까지의 비용 비교 => 더 짧은 노드로 테이블 갱신
# 1 - 2 / 1 - 3 / 1 - 4 인접 노드 확인
# 1에서 2로 거쳐갈 때의 비용은 2. 현재 무한이므로 값 비교후 업데이트
graph = {
    1: [{2: 2}, {3: 5}, {4: 1}],
    2: [{3: 3}, {4: 2}],
    3: [{2:3}, {6: 5}],
    4: [{3:3}, {5: 1}],
    5: [{6:2}, {3:1}],
    6: [{}]
}

node = [1, 2, 3, 4, 5, 6]
distance = [int(1e9)] * len(node)
status = [False] * len(node)

# 출발 노드에서 출발 노드의 거리는 0
distance[0] = 0

test = [0, 3, 1, 4, 5]
# step 1
for t in test:
    myStep = node[t]
    myStepIndex = node.index(node[t])
    for i in graph[myStep]:
        if len(i.keys()) > 0:
            key = list(i.keys())[0] - 1
            value = list(i.values())[0]
            cal = distance[myStepIndex] + value
            if cal < distance[key]:
                distance[key] = cal
    status[myStepIndex] = True
    print(distance)
print(status)

# step 2
# firstStepIndex를 제외하고 최솟값을 찾아야함
# pass
# myStep = node[3]
# myStepIndex = node.index(node[3])
# # print(myStep) #    4
# # print(myStepIndex) #3
# for i in graph[myStep]:
#     key = list(i.keys())[0] - 1
#     value = list(i.values())[0]
#     # print(key, value)
#     # print(f"해당 노드에서 갈 수 있는 노드 Index {key}")
#     # print(f"해당 노드에서 최단거리 {distance[myStepIndex]}")
#     cal = distance[myStepIndex] + value
#     # print(f"계산 = {cal}")
#     # print(distance[key])
#     if cal < distance[key]:
#         distance[key] = cal
# # print(distance)
#
# # step 3
# # distance index 0, 3 제외하고 최솟값을 찾아야함
# # index 1, 4 노드를 선택해야함.
# myStep = node[1]
# myStepIndex = node.index(node[1])
# # print(myStep) #    4
# # print(myStepIndex) #3
# for i in graph[myStep]:
#     key = list(i.keys())[0] - 1
#     value = list(i.values())[0]
#     # print(key, value)
#     # print(f"해당 노드에서 갈 수 있는 노드 Index {key}")
#     # print(f"해당 노드에서 최단거리 {distance[myStepIndex]}")
#     cal = distance[myStepIndex] + value
#     # print(f"계산 = {cal}")
#     # print(distance[key])
#     if cal < distance[key]:
#         distance[key] = cal
# print(distance)