# 퀵 정렬(재귀함수 구현)
- 기준값을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복해 정렬하는 알고리즘
- 평균 시간 복잡도 O(nlogn) / 최악의 경우 시간 복잡도 O(n^2)
- pivot을 중심으로 계속 데이터를 2개의 집합으로 나누면서 정렬

# 퀵 정렬 과정
1. 데이터를 분할하는 pivot을 설정한다.
2. pivot을 기준으로 다음 과정을 거쳐 데이터를 2개의 집합으로 분리
   1. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면 start를 오른쪽으로 1칸 이동
   2. end가 가리키는 데이터가 pivot이 가리키는 데이터보다 크면 end를 왼쪽으로 1칸 이동
   3. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 크고, end가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면
start, end가 가리키는 데이터를 swap하고 start는 오른쪽, end는 왼쪽으로 1칸씩 이동
   4. start와 end가 만날 때 까지 2-1~2-3 반복
   5. start와 end가 만난다면 만난 지점에서 가리키는 데이터와 pivot이 가리키는 데이터를 비교해 pivot이 가리키는 데이터가 크면 
만난 지점의 오른쪽에, 작으면 만난 지점의 왼쪽에 pivot이 가리키는 데이터를 삽입
3. 분리 집합에서 각각 다시 pivot을 선정
4. 분리 집합이 1개 이하가 될 때까지 과정 1~3을 반복