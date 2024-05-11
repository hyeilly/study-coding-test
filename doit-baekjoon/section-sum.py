# 합 배열 S를 만드는 공식
# S[i] = S[i-1] + A[i]

# 구간 합 : S[j] - S[i-1]

# 구간 합 구하기2
# N x N
# (X1,Y1), (X2, Y2)
N = 4
x1, y1 = 4, 2
x2, y2 = 3, 4
tu = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
]
answer = 0
for i in range(x1-1, x2):
    for j in range(x1-1, y2):
        print(f"i:{i} j:{j} tu[i][j]:{tu[i][j]}")
        answer += tu[i][j]
print(answer)


