# 정렬을 사용하면 시간복잡도 문제 있음
# 슬라이딩 윈도우를 덱(deque)으로 구현해서 정렬 효과
# 데이터를 양쪽으로 넣었다 뺐다
# 1. 최소값 가능성이 없는 데이터 삭제
# 2. 윈도우 크기 밖으로 넘어간 데이터 삭제
# N, L = 12 3
# now = 1 5 2 3 6 2 3 7 3 5 2 6
import sys
from collections import deque

input = sys.stdin.readline
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 나보다 큰 데이터 삭제
    # 나의 deque 가장 끝에 있는 값이 더 크면
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    # 슬라이딩 윈도우를 벗어난 데이터 삭제
    # 내 deque의 맨 첫번째 인덱스가 현재 들어온 데이터와 비교
    if mydeque[0][1] <= i-L:
        mydeque.popleft()

    print(mydeque[0][0], end=' ')
