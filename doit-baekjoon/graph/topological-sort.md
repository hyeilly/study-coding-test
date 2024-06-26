# 위상 정렬
- 사이클이 없는 방향 그래프에서 노드 순서를 찾는 알고리즘
- 기능 : 노드 간의 순서를 결정
- 특징 : 사이클이 없어야 함
- 시간복잡도(노드 수:V, 에지 수:E) : O(V + E)
- 항상 유일한 값으로 정렬되지 않음
- 사이클이 존재하면 노드 간의 순서를 명확하게 정의할 수 없으므로 위상 정렬 적용할 수 없음

# 위상 정렬 원리
1. 진입 차수(자기 자신을 가리키는 에지의 개수)
2. 진입 차수 배열에서 진입 차수가 0인 노드를 선택하고 선택된 노드를 정렬 배열에 저장. 
- 그 후 인접 리스트에서 선택된 노드가 가리키는 노드들의 진입 차수를 1씩 뺌

# 위상 정렬 수행 과정
1. 진입 차수가 0인 노드를 큐에 저장
2. 큐에서 데이터를 poll해 해당 노드를 탐색 결과에 추가하고, 해당 노드가 가리키는 노드의 진입 차수를 1씩 감소
3. 감소했을 때 진입 차수가 0이 되는 노드를 큐에 offer 
4. 큐가 빌 때까지 1 ~ 3 반복