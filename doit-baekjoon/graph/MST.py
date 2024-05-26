# 입력 1 : 노드의 개수 V(1<=V<=10,000) / 에지의 개수 E(1<=E<=100,000)
# 입력 2 : 에지와 관련된 정보 세 정수 A, B, C => A번 노드, B번 노드 , 가중치 C인 에지로 연결
# 그래프의 노드는 1번부터 V번까지 번호 매겨져 있고, 임의의 두 노드 사이 경로가 있음
# -2,147,483,648 <= 가중치 <= 2,147,483,648 데이터 입력 => Int 자료형 범위
from queue import PriorityQueue
V, E = 3, 3
idx_list = [i for i in range(V+1)]

def find(target):
    if idx_list[target] == target:
        return target
    else:
        # find(idx_list[target])
        idx_list[target] = find(idx_list[target])
        return idx_list[target]

def union(data, w):
    idx_list[data] = w
    return idx_list

# 가중치 기준으로 오름차순 정렬 => 우선순위큐를 사용하면 자동정렬
pq = PriorityQueue()
pq.put((1, 1, 2))
pq.put((2, 2, 3))
pq.put((3, 1, 3))
result = 0
node = 0
# list = sorted(list, key=lambda l: l[2])
while pq.qsize() > 0:
    current = pq.get()
    w, a, b = current
    # union_find(idx_list, a, b)
    print(f"node a: {a} / node b: {b} / w: {w}")
    if find(a) != find(b):
        union(b, w)
    node += 1
    if node < V:
        result += w
print(result)

# 크루스칼 알고리즘 수행
# 사이클이 발생하지 않으면 에지값 더하기


