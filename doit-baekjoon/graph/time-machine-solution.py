# 타임머신으로 빨리가기
# N개의 도시, 한 도시에서 출발해 다른 도시에 도착하는 버스 M개
# 각 버스는 A, B, C로 나타낼 수 있음
# A는 시작 도시, B는 도착 도시, C는 버스를 타고 이동하는데 걸리는 시간
# 시간 C=0일 경우 순간이동할 때, C<0일 경우에는 타임머신으로 시간을 되돌아감

# 3 4
# 1 2 4
# 1 3 3
# 2 3 -4
# 3 1 -2

import sys
input = sys.stdin.read
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1) # 첫번째 도시를 첫번째 인덱스로 세팅하기 위해

# 에지 데이터 저장
for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 시작 도시는 0으로 초기화
distance[1] = 0

for _ in range(N - 1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] * time
mCycle = False
# 한번더 돌리기 => 음수 사이클 있는지 확인
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True

if not mCycle:
    # 두번째 도시부터 출력
    for i in range(2, N + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)