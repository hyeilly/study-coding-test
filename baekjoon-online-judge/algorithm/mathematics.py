def sum_cycle():
    n = int(input())

    num = n
    cnt = 0

    while True:
        a = num // 10 # 10의 자리
        b = num % 10 # 1의 자리
        c = (a + b) % 10 # 합한 것의 1의 자리
        num = (b * 10) + c

        cnt += 1
        if (num == n):
            break
    print(cnt)
def count_number():
    A = int(input())
    B = int(input())
    C = int(input())
    result = str(A * B * C)
    li = [0 for _ in range(10)]
    for i in result:
        li[int(i)] += 1
    for l in li:
        print(l)

def sumAB():
    A = int(input())
    B = int(input())
    print(A + B)

def factorial():
    A = int(input())
    result = 1
    while(A != 0):
        result *= A
        A -= 1
    print(result)

def exceed_avg():
    num = int(input())
    for _ in range(num):
        sList = list(map(int, input().split()))
        s = sList[0]
        s_list = sList[1:]
        avg = sum(s_list) / s
        cnt = 0
        for S in s_list:
            if avg < S:
                cnt += 1
        rate = cnt / s * 100
        print(f'{rate:.3f}%')



