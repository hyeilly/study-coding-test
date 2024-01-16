# 팀 결성
# 0번부터 N번까지 번호 부여
# 1. '팀 합치기' - 두 팀을 합치는 연산
# 2. '같은 팀 여부 확인' - 특정 두 학생이 같은 팀에 속하는지 확인

def find_parent(parent, x):
    print(f"find_parent 실행- parent:{parent} x:{x}")
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        print(f"재귀호출")
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    print(f"a: {a} b:{b}")
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N, M = map(int, input().split())
N, M = 7, 8
# 팀 합치기 연산은 u = 0
# 같은 팀 여부 확인 u = 1
# for _ in range(M):
#     u, a, b = map(int, input().split())
# 부모 테이블에서 부모노드 초기화
parent_node = []
for i in range(N + 1):
    parent_node.append(i)
# a번 학생이 속한 팀과 b번 학생이 속한 팀을 합치기
u, a, b = 0, 1, 3
print(parent_node[a])
print(parent_node[b])
if u == 0:
    union_parent(parent_node, a, b)
elif u == 1:
    if find_parent(parent_node, a) == find_parent(parent_node, b):
        print('YES')
    else:
        print('NO')