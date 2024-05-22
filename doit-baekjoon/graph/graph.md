# 그래프
- 그래프 : 노드와 에지로 구성된 집합
- 노드 : 데이터를 표현하는 단위이고 에지는 노드를 연결

# 알고리즘
- 유니온 파인드
  - 집합에서 대표 노드 찾기
  - 각각 원소를 유니온하여 하나의 집합으로 만들기
  - 그래프에서는 **그래프의 사이클이 생성되는지 판별하는 알고리즘**
- 위상정렬
  - **사이클이 없고, 방향이 있는 그래프**일때 사용할 수 있음
  - 그래프의 **노드들을 선형으로 정리**
  - 값이 유일하지 않음 
  - ex) 수강신청(전후 관계가 있어야함)
- 다익스트라 / 벨만-포드 / 플로이드-워셜
  - 노드에서 노드 사이 최단거리 알고리즘
  - 다익스트라
    - S 시작점 고정되어있고, 
    - S 시작점에서 다른 모든 노드로 가는 최단거리를 구하는 알고리즘
    - 제약사항) 음수 간선은 안됨. 
  - 벨만-포드
    - 다익스트라와 의미는 같지만 음수 간선도 가능함
    - 음수 사이클이 있는지 확인하는 문제 많이 나옴
  - 플로이드-워셜
    - 시작점이 없고, 주어진 모든 노드 중 어떤 걸 체크하더라도 최단거리를 구할 수 있음
    - 시간복잡도가 안좋음  
    - ex)모든 도시 간 최단 거리 구해야하는데 도시 개수 N,(N이 작을 때) 쓰기
- 최소 신장 트리(MST) 
  - 최소의 가중치 합으로 모든 노드를 연결할 수 있게 해줌
  - 간선의 가중치가 최소가 되도록 
  - 사이클이 없음