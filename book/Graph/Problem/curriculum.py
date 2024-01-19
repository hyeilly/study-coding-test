# 강의가 짧게 걸리는지 확인
# '자료구조', '컴퓨터 기초' 존재한다면 => 모두 들은 후 '알고리즘'강의 듣기 가능
# 1번부터 N번까지의 번호를 가지는 강의
# N = 3
from collections import deque
import copy

# 노드의 개수 입력받기
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
from collections import deque
import copy
#     graph[i].append(i)
# print(indegree)

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)
for i in range(1, v + 1):
    data = list(map(int, input().split()))