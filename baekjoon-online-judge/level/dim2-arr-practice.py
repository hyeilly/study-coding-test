n, m = map(int, input().split())
n_a, m_a = [], []
for _ in range(n):
    n_arr = list(map(int, input().split()))
    n_a.append(n_arr)
for _ in range(m):
    m_arr = list(map(int, input().split()))
    m_a.append(m_arr)
for i in range(n):
    res = []
    for k in range(len(n_a[i])):
        res.append(n_a[i][k] + m_a[i][k])
    for r in res:
        print(r, end=' ')
    if i < n - 1:
        print()
