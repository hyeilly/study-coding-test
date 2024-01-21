# 1. 공포도 기준 오름차순
# 2. 공포도 가장 낮은 모험가부터 하나씩 확인
# => 그룹에 포함될 모험가 수 계산

n = int(input())
data = list(map(int, input().split()))
data.sort()
print(f"sort: {data}")

# 총 그룹의 수
result = 0
# 현재 그룹에 포함된 모험가의 수
count = 0

# 공포도를 낮은 것부터 하나씩 확인
for i in data:
    # 현재 그룹에 해당 모험가를 포함시키기
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
    print(f"count: {count} i:{i} 비교")
    if count >= i:
        # 총 그룹의 수 증가시키기
        result += 1
        # 현재 그룹에 포함된 모험가의 수 초기화
        count = 0
        print(f"i: {i} count: {count} result: {result}")
print(result)