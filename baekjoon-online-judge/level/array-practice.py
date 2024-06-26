import sys
def find_num():
    N = int(input())
    list = list(map(int, input().split()))
    find = int(input())
    cnt = 0
    for l in list:
        if find == l: cnt += 1
    print(cnt)

def print_num():
    N, X = map(int, input().split())
    list = list(map(int, input().split()))
    for l in list:
        if l < X:
            print(l, end=' ')

def min_max():
    N = int(input())
    list = list(map(int, input().split()))
    print(min(list), max(list))

def input_ball():
    N, M = map(int, input().split())
    list = [0 for _ in range(N)]

    for _ in range(M):
        i, j, k = map(int, input().split())
        for bucket in range(i - 1, j):
            list[bucket] = k
    for a in list:
        print(a, end=' ')

def change_ball():
    N, M = map(int, input().split())
    list = [i for i in range(1, N + 1)]
    for _ in range(M):
        i, j = map(int, input().split())
        temp = list[i - 1]
        list[i - 1] = list[j - 1]
        list[j - 1] = temp
    for a in list:
        print(a, end=' ')

def attendance():
    input = sys.stdin.readline
    student = [i for i in range(1, 31)]
    for _ in range(28):
        num = int(input())
        student.remove(num)
    for s in student:
        print(s)

def remain():
    list = []
    for _ in range(10):
        data = int(input())
        list.append(data%42)
    print(len(set(list)))

def reverse_ball():
    N, M = map(int, input().split())
    list = [i for i in range(1, N + 1)]
    for _ in range(M):
        i, j = map(int, input().split())
        reverse_list = list[i - 1 : j]
        list = list[0:i-1] + reverse_list[::-1] + list[j:]
    for l in list:
        print(l, end=' ')

def calc_avg():
    # 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답
    # => 소수점 제한없이 출력
    N = int(input())
    score = list(map(int, input().split()))
    M = max(score)
    for (sdx, s) in enumerate(score):
        fix = float(s / M * 100)
        score[sdx] = fix

    total = 0
    for i in score:
        total += i
    print(float(total / N))

