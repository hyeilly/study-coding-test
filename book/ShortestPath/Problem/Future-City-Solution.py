# 공중 미래 도시 1번 ~ N번까지 회사 있음
# 방문 판매원 A는 1번 회사 위치 - X번 회사에 방문해 물건 판매
# 연결된 2개의 회사는 양방향으로 이동 가능
# 공중 미래 도시 - 도로는 마하의 속도로 사람 이동
# 특정 회사와 다른 회사가 도로로 연결 => 정확히 1만큼 시간으로 이동
# 오늘 방문 판매원 A는 소개팅 참석
# 소개팅의 상대는 K번 회사에 존재
# 방문 판매원 A는 X번 회사에 가서 물건 판매하기 전 먼저 소개팅 상대 회사 찾아가 함께 커피 마실 예정
# 방문 판매원 A는 1번 회사에서 출발해 K 번 회사를 방문한 뒤 X번 회사로 가는 것이 목표
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
# 첫번째 줄 입력 받는 부분
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]


# 방문판매원 A가 최종적으로 4번 회사에 가는 경로를 (1번-3번-5번-4번) 설정
# 소개팅에도 참석할 수 있으면서 총 3만큼의 시간으로 이동
# 이 경우 최소 이동시간은 3

# N의 범위가 주어짐 - 구현이 간단한 플로이드 워셜 알고리즘 이용
# 1번 노드에서 X를 거쳐 K로 가는 최단 거리
# (1번 노드에서 X까지의 최단 거리 + X에서 K까지의 최단 거리)


# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# (1, 1),(2, 2),(3, 3),(4, 4)
# print(graph)
# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+ 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)