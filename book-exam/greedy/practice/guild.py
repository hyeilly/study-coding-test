# 모험가 N 명
# '공포도' 측정
# 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성
N = 5
scary = [2, 3, 1, 2, 2]
# N = int(input())
# scary = map(int, input().split())

scary.sort()
cnt = 0
max_v = 0
result = 0

for i in scary:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(result)