n = int(input())
data = list(map(int, input().split()))
data.sort()

# 총 그룹 수
result = 0
# 현재 그룹에 포함된 모험가의 수
count = 0
# 공포도 낮은 것 부터 하나씩 확인
for i in data:
    # 현재 그룹에 해당 모험가를 포함
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
    if count >= i:
        # 총 그룹의 수 증가
        result += 1
        # 현재 그룹에 포함된 모험가의 수 초기화
        count = 0
# 총 그룹의 수 출력
print(result)