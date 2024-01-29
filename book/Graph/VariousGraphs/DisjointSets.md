# 서로소 집합
- 공통 원소가 없는 두 집합
- 집합 {1, 2}와 집합 {3, 4}는 서로소 관계
- 집합 {1, 2}와 집합 {2, 3}은 원소 2가 두 집합에 공통 포함 => 서로소 관계 아님
## 서로소 집합 자료구조
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- union
  - 2개의 원소가 포함된 집합을 하나의 집합으로 합치기
- find
  - 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- 트리 자료구조 이용해 집합 표현하는 알고리즘
  1. union(합집합) 연사나 확인해 서로 연결된 두 노드 A, B 확인
     - A와 B의 루트 노드 A', B'를 찾음
     - A'를 B'의 부모 노드로 설정(B'가 A'를 가리키도록 함)
  2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정 반복
   => A'와 B' 중 더 번호가 작은 원소가 부모 노드가 되도록 구현되는 경우가 많음
   트리를 이용해 서로소 집합 계산하는 알고리즘
### 예시
- 집합 [1, 2, 3, 4, 5, 6] 6개 원소로 구성, 4개의 union 연산
  - union 1,4 / union 2, 3 / union 2, 4 / union 5, 6
  - 4개의 union 연산 수행 후 전체 원소들이 결과적으로 어떤 형태의 부분집합으로 나누어질지?
  - 전체원소 [1, 2, 3, 4], [5, 6] 2개의 집합으로 나누어짐

## 서로소 집합 알고리즘의 시간 복잡도
- 노드개수 V
- 최대 V - 1개의 union 연산
- M개의 find 연산 
- => 경로 압축 방법을 적용한 시간 복잡도 = O(V + M(1 + log(2-M/V)V))

## 서로소 집합 활용한 사이클 판별
- 무방향 그래프 내에서의 사이클 판별 시 사용 가능
- 방향 그래프에서 사이클 여부는 DFS를 이용해 판별 가능 
- union 연산은 그래프에서의 간선으로 표현 가능
  1. 각 간선을 확인하며 두 노드의 루트 노드 확인
     1. 루트 노드가 서로 다르다면 두 노드에 대하여 union연산 수행
     2. 루트 노드가 서로 같다면 사이클 발생한 것
  2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복