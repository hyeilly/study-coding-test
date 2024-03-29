# 다익스트라 최단 경로 알고리즘
- 그래프에서 여러 개의 노드가 있을 때, 
- 특정한 노드에서 출발해 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- '**음의 간선**'이 없을 때 정상적으로 동작
  - 0보다 작은 값을 가지는 간선
  - 현실 세계의 길(간선)은 음의 간선으로 표현하지 않음
  - GPS 소프트웨어 기본 알고리즘
- 기본적으로 **그리디 알고리즘**으로 분류
  - 매 상황에서 가장 비용 적은 노드 선택해 임의의 과정 반복
  - a에서 c => a에서 b 최단 경로 + b에서 c 최단 경로 고려한 a => c

## 원리  
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
   - 처음은 기본적으로 모든 노드까지 가기 위한 비용을 무한으로 설정
   - 자기 자신에 대한 노드는 0으로 설정
   - (=자기 자신에서 자기 자신으로 가는 비용은 0)
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
4. 해당 노드 거쳐 다른 노드로 가는 비용 계산해 최단 거리 테이블 갱신
5. 3번과 4번 반복

## 최단 경로를 구하는 과정
- 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장 후 리스트 계속 갱신
- 매번 현재 처리하고 있는 노드 기준으로 주변 간선 확인 
- 나중에 현재 처리하고 있는 노드와 인접한 노드로 도달하는 **더 짧은 경로 찾으면 채택**
- 방문하지 않은 노드 중에서 현재 최단 거리가 가장 짧은 노드 확인 => 4번 과정 수행

## 구현하는 방법
- 방법1) 구현하기 쉽지만 느리게 동작하는 코드
- 방법2) 구현하기 까다롭지만 빠르게 동작하는 코드 

## Example
- 1번 노드에서 다른 모든 노드로 가는 최단 경로
- 초기상태 = 다른 모든 노드로 가는 최단 거리 '무한'으로 초기화
  - 모든 간선이 정수형 표현되는 문제의 경우 `int(1e9)`로 초기화

# 구현
- 시간 복잡도 O(V^2)
1. 각 노드에 대한 최단 거리 담는 1차원 리스트 선언
2. 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소 확인(순차 탐색)
- 총 O(V)번 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색 해야함 
- 현재 노드와 연결된 노드를 일일이 확인해야함 
- 전체 노드 개수가 10,000개 넘어간다면 개선된 다익스트라 알고리즘 이용해야함 (Practice2.py)