# 가장 빠른 버스 노선 구하기
# 시간제한 1초
# n(2<=n<=100) 개의 도시
# 한 도시에서 출발, 다른 도시로 도착 m(1<=m<=100,000)
# 모든 도시 쌍(A,B)에 관해 A에서 B로 가는데 필요한 비용의 최솟값(=최단거리)

# 플로이드 워셜 알고리즘 문제

# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

# S = int(input())
# E = int(input())
import math
N, M = 5, 14
data = [
[1, 2, 2],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3],
[3, 5, 8],
[1, 4, 2],
[5, 1, 7],
[3, 4, 2],
[5, 2, 4],
]
array = []
# 초기화
for a in range(N+1):
    array_a = []
    for i in range(N+1):
        if a == i:
            array_a.append(0)
        else:
            array_a.append(float('INF'))
    array.append(array_a)
for start, end, edge in data:
    # 최단거리이므로 작은 값 저장
    original = array[start][end]
    if original > edge:
        array[start][end] = edge
print(array)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if array[i][j] > array[i][k] + array[k][j]:
                array[i][j] = array[i][k] + array[k][j]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if array[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(array[i][j], end=' ')
    print()