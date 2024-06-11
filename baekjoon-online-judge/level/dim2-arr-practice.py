def procession_sum():
    n, m = map(int, input().split())
    n_a, m_a = [], []
    for _ in range(n):
        n_arr = list(map(int, input().split()))
        n_a.append(n_arr)
    for _ in range(n):
        m_arr = list(map(int, input().split()))
        m_a.append(m_arr)

    for i in range(n):
        for k in range(len(n_a[i])):
            print(n_a[i][k] + m_a[i][k], end=' ')
        print()
def procession_max():
    arr = []
    for _ in range(9):
        li = list(map(int, input().split()))
        arr.append(li)

    temp = 0
    temp_row = 0
    temp_column = 0

    for (adx, a) in enumerate(arr):
        if temp <= max(a):
            temp = max(a)
            temp_row = adx + 1
            temp_column = a.index(temp) + 1
    print(temp)
    print(temp_row, temp_column)

arr = []
for _ in range(5):
    input_data = list(input())
    arr.append(input_data)

result = ''

print(len(arr))
