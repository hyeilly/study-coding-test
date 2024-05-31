# 최소 공통 조상 구하기1 (일반적인 방법으로 가능)

# N(2<=N<=50,000)개 노드
# 트리 각 노드는 1번 ~ N번 까지 번호
# 루트는 1번
# 두 노드의 쌍 M(1<=M<=10,000) 개 주어졌을 때 두 노드 가장 가까운 공통 조상
from collections import deque

N = 15 # 노드 개수
N_link = [
    [1, 2], [1, 3], [2, 4], [3, 7], [6, 2], [3, 8], [4, 9], [2, 5],
    [5, 11], [7, 13], [10, 4], [11, 15], [12, 5], [14, 7]
]
M = 6 # 질의 개수 최소공통조상 알고 싶은 것들
M_link = [
    [6, 11], [10, 9], [2, 6], [7, 6], [8, 13], [8, 15]
]

def LCA():
    pass

parent_node = [0 for i in range(N+1)]
depth_node = [0 for i in range(N+1)]
root = 1
for n in N_link:
    n1, n2 = n
    parent = n1
    child = n2
    if n1 > n2:
        parent = n2
        child = n1
    parent_node[child] = parent
print(parent_node)
queue = deque()
queue.append(root)
depth = 1
for (pdx, p) in enumerate(parent_node):
    if pdx > 0:
        print(queue)
        point = queue.popleft()

        idx_list = list(filter(lambda x: parent_node[x] == point, range(len(parent_node))))
        idx_list_len = len(idx_list)
        print(f"p:{p} - pdx:{pdx} - idx_list: {idx_list} - depth:{depth}")
        for i in idx_list:
            queue.append(i)







print(depth_node)