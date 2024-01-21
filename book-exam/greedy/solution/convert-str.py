# 전체 리스트의 원소 앞에서부터 하나씩 확인
# 0에서 1로 변경하거나 1에서 0으로 변경하는 경우
# example 0001100
data = input()
# 전부 0으로 바꾸는 경우
count0 = 0
# 전부 1으로 바꾸는 경우
count1 = 0

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소 확인
for i in range(len(data) - 1):
    print(f"두 번째 원소부터 확인i: {i}")
    if data[i] != data[i + 1]:
        # 다음 수에서 1으로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
print(min(count0, count1))