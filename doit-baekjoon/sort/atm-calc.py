# ATM 1대 . N명 사람들 줄 서있음. 1번에서 N번까지 번호 매겨짐
#(1, 3), (2, 1), (3, 4), (4, 3), (5, 2) 몇번째 사람이 돈 뽑는데 걸리는 시간


N = 5
P = [3, 1, 4, 3, 2]

P_sort = sorted(P)
for (idx, i) in enumerate(P_sort):
    if idx > 0:
        P_sort[idx] += P_sort[idx-1]
print(P_sort)
answer = sum(P_sort)
print(answer)