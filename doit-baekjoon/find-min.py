# 최솟값 찾기1
# 1번째 줄에 N과 L
# N개의 수 Ai
# N개의 수 A1, A2,..., AN
# 최솟값을 Di 라고 할 때 D에 저장된 수를 출력하는 프로그램
# i<=0인 Ai 는 무시하고 D를 구해야함

N, L = map(int, input().split())
D = list(map(int, input().split()))

# N, L = 12, 3
# D = [1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]
answer_array = []


for i in range(N):
    check_array = []
    window = []
    window.append(i)
    for l in range(1, L):
        window_data = 0 if i - l < 0 else i - l
        window.append(window_data)
    for w in window:
        check_array.append(D[w])
    answer_array.append(str(min(check_array)))

print(' '.join(answer_array))
