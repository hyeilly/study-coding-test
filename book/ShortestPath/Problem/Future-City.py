# 첫째 줄 : 전체 회사의 개수 N, 경로의 개수 M (1<=N, M<=100)
# 둘째 줄 : M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어짐
# M + 2번째 줄에는 X, K 가 공백으로 구분되어 차례로 (1<=K<=100)
# A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간

INF = int(1e9)
# N, M = map(int, input().split())
N, M = 5, 7
# print(N, M)
# 2차원 리스트 만들기
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            # 자기 자신으로 가는 비용은 0
            graph[a][b] = 0

# 경로 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    # 거쳐서 가는 경로이므로
    graph[a][b] = 1
    graph[b][a] = 1
print(graph)
# 최종 목적지 입력받기
x, k = map(int, input().split())
# k 를 거쳐가는 것
for k in range(1, N + 1):
    # a부터
    for a in range(1, N +1 ):
        # b까지 가는데
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

# 1부터 x까지 가는 거리 계산
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print('-1')
else:
    print(distance)


