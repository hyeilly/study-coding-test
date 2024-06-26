# 트리
- 노드와 에지로 연결된 _그래프의 특수한 형태_
  - 그래프의 표현으로도 tree 표현 가능

# 트리의 특징
- 순환 구조를 지니고 있지 않고, 1개의 루트 노드가 존재
- 루트 노드를 제외한 노드는 단 1개의 부모 노드를 가짐
- 트리의 부분 트리 역시 트리의 모든 특징을 따름
- => 트리에서 임의의 노드 두개를 이어주는 경로는 유일하게 1개

# 트리의 구성 요소
- 노드 : 데이터의 index와 value를 표현하는 요소
- 에지 : 노드와 노드의 연결 관계를 나타내는 선
- 루트 노드 : 트리에서 가장 상위에 존재하는 노드
- 부모 노드 : 두 노드 사이의 관계에서 상위 노드에 해당하는 노드
- 자식 노드 : 두 노드 사이의 관계에서 하위 노드에 해당하는 노드
- 리프 노드 : 트리에서 가장 하위에 존재하는 노드(자식 노드가 없는 노드)
- 서브 트리 : 전체 트리에 속한 작은 트리

# 코딩테스트에서는...
## 그래프로 푸는 tree
- 트리에 노드, 에지가 있음
  - 인접리스트로 표현 가능 
    - => 그래프 탐색 시 탐색 알고리즘 중 가장 많이 나오는 DFS BFS 
- DFS, BFS 적용해서 푸는 tree 문제가 있음
  **- tree를 그래프 처럼 인접리스트로 표현해서 DFS, BFS로 문제 해결**

## tree만을 위한 문제
- 트리 중에서도 이진트리, **세그먼트 트리(index tree)**, LCA(최소 공통 조상)
- 1차원 배열로 트리를 표현 
  - \[0, A, B, C, D, E]
  - 트리에서는 부모/자식을 따지는 것 중요
  - 부모 노드로 이동하는 것은 **자신의 index/2**
  - 자식노드로 이동하는 것은 **(index * 2) + 1**