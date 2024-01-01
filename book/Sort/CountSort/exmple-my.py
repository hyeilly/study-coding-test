array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 가장 큰 데이터와 가장 작은 데이터의 범위 모두 담을 수 있는 하나 리스트 생성
# 모든 데이터는 0으로 초기화
array_list = [0 for i in range(min(array), max(array) + 1)]
# 등장한 횟수로 카운트 증가
for i in array:
    array_list[i] += 1
print(array_list)
result = ''
for (adx, a) in enumerate(array_list):
    for i in range(a):
        result += str(adx) + " "
print(result)
