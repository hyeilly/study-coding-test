# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    print(f"parent찾기 : parent[x]:{parent[x]} x:{x}")
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 노드 5의 루트 찾기 위해 노드5 ~ 노드1 순서대로 부모노드 거슬러 올라감 => O(V)
# 경로 압축 기법(path compression)
def find_parent_path_comp(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_path_comp(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    print(f"union parent: {parent}")

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)
print(f"parent 초기화: {parent}")

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    print(f"부모 테이블 자기 자신 초기화 {parent}")

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')