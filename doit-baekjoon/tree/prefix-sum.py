# 구간 합 구하기3
# 세그먼트 트리 문제

# 어떤 N개의 수가 주어짐. 중간에 수의 변경이 빈번하게 일어나고, 그 중간에 어떤 부분의 합을 구하려고함
# 부분의 합 : 합배열 또는 세그먼트(인덱스) 트리로 구하기

N, M, K = 5, 2, 2
N_list = [1, 2, 3, 4, 5]
# a가 1일때는 데이터의 변경
# a가 2일때는 b에서 c까지의 부분합을 구해 출력
list = [
    [1, 3, 6],
    [2, 2, 5],
    [1, 5, 2],
    [2, 3, 5]
]

# 2^k >= N = 2^3 >= 5 => 2^3 * 2 = 16
li = [0 for i in range(16)]
# 1차원 배열 트리 값 초기화
start_index = 8
j = 0
for i in range(start_index, start_index + len(N_list)):
    li[i] = N_list[j]
    j += 1

# 트리로 봤을 때 배열 크기 16인 이유
# 리프 노드가 첫 오리지널 데이터 보다 커야함 => N=5
# 이진트리 생김
for i in range(len(li)-1, 1, -1):
    li[int(i / 2)] += li[i]
print(li)
result = 0
# 질의 값 연산 함수와 데이터 업데이트 함수 수행
# 질의와 관련된 결과값 추가
for type, a, b in list:
    if type == 1:
        # a 를 b로 업데이트
        idx = start_index + a - 1
        sum = b - li[idx]
        while (idx > 1):
            li[idx] += sum
            idx = int(idx / 2)
            if idx == 1:
                break
    elif type == 2:
        # 구간합
        start = a+start_index-1
        end = b+start_index-1

        while start < end:
            result += li[start] + li[end]
            if start > end:
                break
            if start % 2 == 1:
                # 단독노드임. 이 부모노드가 아닌 한칸 위로 가기 위해
                start = int((start + 1) / 2)
                result += li[start]
            if end % 2 == 0:
                end = int((end - 1) / 2)
        print(result)
print(li)