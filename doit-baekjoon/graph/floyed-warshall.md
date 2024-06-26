# 플로이드-워셜
- 최단 거리를 구하는 알고리즘
- 기능: **모든 노드** 간에 최단 경로 탐색
- 특징
  - 음수 가중치 에지가 있어도 수행할 수 있음
    - 음수 사이클이 있으면 안됨
  - 동적 계획법의 원리를 이용해 알고리즘에 접근
- 시간복잡도(노드수 : V): O(V^3)
  - 시간복잡도가 안좋아 대부분 노드는 200, 100으로 나올 것.

# 플로이드-워셜 핵심 이론
- A노드에서 B노드까지 최단 경로를 구했다고 가정
- 최단 경로 위에 K 노드가 존재한다면 그것을 이루는 부분 경로 역시 최단 경로
## 점화식
- D\[S][E] = Math.min(D\[S][E], D\[S][K] + D\[K][E])
  - K는 S,E 사이에 있는 모든 경로를 이야기함
## 알고리즘 구현 방식
1. 리스트를 선언하고 초기화
   - Node의 개수가 적을 수 밖에 없어 인접행렬으로 최단 거리 리스트를 만들 수 있음(2차원 리스트)
   - 자기 자신에게 걸리는 시간은 0으로 초기화, 다른 칸들은 무한대
2. 최단 거리 리스트에 그래프 데이터 저장하기 
  - 출발노드 S, 도착노드 E, 가중치 W 
  - D\[S][E] = W로 에지의 정보를 리스트에 입력 
3. 점화식으로 리스트에 업데이트
   - 3중 for문으로 리스트 값 업데이트
   - 가장 바깥 for문이 경유지 K, 두번째 for문 출발노드 S , 세번째 for문 도착노드 E 
   - 최단 거리 리스트가 모든 쌍 노드에 대한 최단거리 표현 