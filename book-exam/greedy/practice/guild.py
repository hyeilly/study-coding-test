# 모험가 길드
# N명 모험가 대상으로 '공포도'측정 => 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처 X
# 공포도가 X인 모험가는 반드시 X명 이상 구성한 모험가 그룹 참여
n = int(input())
scary = list(map(int, input().split()))
scary.sort()
print(scary)

