# 다익스트라 알고리즘
- 최단 거리를 구하는 알고리즘
- 기능 : 출발 노드와 모든 노드 간의 최단 거리 탐색
- 특징 : 에지는 모두 양수
- 시간 복잡도(노드 수: V, 에지 수: E) : O(ElogV)

# 다익스트라 알고리즘 핵심 이론
1. 인접 리스트로 그래프 구현하기
- 시간 복잡도 측면 N의 크기가 큰 것을 대비해 인접 리스트를 선택해 구현하는 것이 좋음
2. 최단 거리 배열 초기화
- 출발 노드는 0, 이외는 모두 무한으로 초기화
- 무한은 적당히 큰 값 사용
3. 값이 가장 작은 노드 고르기
- 최단 거리 배열에서 현재 값이 가장 작은 노드 고르기
- 여기서는 값이 0인 출발 노드에서 시작
4. 최단 거리 배열 업데이트하기
- 선택된 노드에서 연결된 에지의 값을 바탕으로 다른 노드의 값 업데이트
- 1단계에서 저장해 놓은 연결 리스트를 이용해 현재 선택된 노드의 에지들을 탐색하고 업데이트
- 연결 노드의 최단 거리는 다음과 같이 두 값 중 더 작은 값으로 업데이트
- 업데이트 방법 : Min(선택 노드의 최단 거리 배열의 값 + 에지 가중치, 연결 노드의 최단 거리 배열의 값)
5. 과정 3~4를 반복해 최단 거리 배열 완성하기
- 모든 노드가 처리될 때까지 과정 3~4 반복
- 과정 4에서 선택 노드가 될 때마다 다시 선택되지 않도록 방문 배열 만들어 처리
- 모든 노드가 선택될 때까지 반복하면 최단 거리 배열이 완성