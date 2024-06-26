import sys


input = sys.stdin.readline
result = 0

def merge_sort(s, e):
    global result
    if e - s < 1: return
    m = int(s +(e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s # 실제 A배열에서 어느 위치에 데이터가 들어가야하는지 나타내는 인덱스
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # index2에서 현재 k 값 빼면 현재 남아있는 앞에있는 데이터의 개수 => swap값 카운트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

tmp = [0] * int(N + 1)
merge_sort(1, N)
print(result)
