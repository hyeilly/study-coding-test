# 트리의 부모 찾기
# 루트 없는 트리 주어짐. 트리의 루트를 1이라고 정했을 때 각 노드의 부모를 구하는 프로그램
# 입력: 1번째 줄에 노드의 개수 N(2<=N<=100,000) , 2번째 줄 부터 N-1개의 줄에 트리상에 연결된 두 노드
# 출력: 1번째 줄부터 N - 1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

# 주어지는 데이터가 단순하게 연결돼 있는 두 노드를 알려줌
# 데이터를 저장 시 양방향 에지를 간주하고 저장
# 트리 저장 시 일반적으로 쓰는 탐색 DFS, BFS
# 트리의 루트가 1이라고 지정돼 있으므로 1번 노드부터 DFS 로 탐색
# 자식 노드로 가기 직전에 현재 노드가 다음 번에 탐색할 노드의 부모노드

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

N = 7
list = [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]
closet = [[] for i in range(N+1)]
visit = [False for i in range(N+1)]
result = [0 for i in range(N+1)]
node = 1

# 인접리스트로 트리 데이터 구현
for parent, child in list:
    closet[child].append(parent)
    closet[parent].append(child)

# DFS 탐색하면서 다음 미방문 노드를 갈 때 부모노드는 현재 노드 저장

visit[0] = True # 사용하지 않는 인덱스 True로 고정
while(not all(visit)):
    visit[node] = True
    before = node
    for i in closet[node]:
        if not visit[i]:
            node = i
    result[node] = before
    print(node)




