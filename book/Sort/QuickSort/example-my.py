array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
# 리스트에서 첫 번째 데이터를 피벗으로 정함
pivot_idx = 0
pivot = array[pivot_idx]
target_A = 0
target_B = 0

# 왼쪽부터 피벗보다 큰 데이터 찾고
for i in range(pivot_idx+1, len(array)):
    if array[i] > pivot:
        target_A = i
        break

# 오른쪽부터 피벗보다 작은 데이터 찾기
for i in range(len(array)-1, pivot_idx, -1):
    if array[i] < pivot:
        target_B = i
        break

# 두 데이터 위치 서로 변경
array[target_A], array[target_B] = array[target_B], array[target_A]
print(array)

pivot_idx += 1

# 왼쪽부터 피벗보다 큰 데이터 찾고
for i in range(pivot_idx+1, len(array)):
    if array[i] > pivot:
        target_A = i
        break

# 오른쪽부터 피벗보다 작은 데이터 찾기
for i in range(len(array)-1, pivot_idx, -1):
    if array[i] < pivot:
        target_B = i
        break

# 두 데이터 위치 서로 변경
array[target_A], array[target_B] = array[target_B], array[target_A]
print(array)

pivot_idx += 1

# 왼쪽부터 피벗보다 큰 데이터 찾고
for i in range(pivot_idx+1, len(array)):
    if array[i] > pivot:
        target_A = i
        break

# 오른쪽부터 피벗보다 작은 데이터 찾기
for i in range(len(array)-1, pivot_idx, -1):
    if array[i] < pivot:
        target_B = i
        break

# 두 값이 엇갈린 경우 작은 데이터와 피벗 위치 서로 변경

if (target_A + 1 == target_B) or (target_A == target_B - 1) or (target_A == target_B + 1) or (target_A == target_B - 1):
    if target_A < target_B:
        target_B = 0
    elif target_B < target_A:
        target_A = 0
# 두 데이터 위치 서로 변경.
array[target_A], array[target_B] = array[target_B], array[target_A]
print(array)
split_array_idx = target_B
print(split_array_idx)

# 분할하기
part1 = array[0:split_array_idx]
part2 = array[split_array_idx+1:]
print(part1)
print(part2)
# 위와 동일한 방법으로 실행