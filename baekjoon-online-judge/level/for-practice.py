import sys
def print_9():
    num = int(input())
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")
def AsumB():
    num = int(input())
    l = []
    for i in range(num):
        li = list(map(int, input().split()))
        l.append(li)
    for list in l:
        print(sum(list))

def accumulate_sum():
    num = int(input())
    result = 0
    for i in range(1, num+1):
        result += i
    print(result)

def receipt():
    total = int(input())
    calc = 0
    N = int(input())
    for i in range(N):
        price, num = map(int, input().split())
        calc += price * num
    if total == calc:
        print('Yes')
    else:
        print('No')

def bytes_print():
    byte = int(input())
    result = ''
    for i in range(byte // 4):
        result += 'long '
    print(result + 'int')

def fast_sum():
    input = sys.stdin.readline
    num = int(input())
    answer = []
    for i in range(num):
        A, B = map(int, input().split())
        answer.append(A + B)
    for a in answer:
        print(a)

def sum_print_type(type):
    num = int(input())
    answer = []
    for i in range(num):
        A, B = map(int, input().split())
        answer.append([A, B])
    for (adx, a) in enumerate(answer):
        A, B = a
        if type == 'simple':
            print(f"Case #{adx + 1}: {sum(a)}")
        else:
            print(f"Case #{adx + 1}: {A} + {B} = {sum(a)}")


def print_star():
    num = int(input())
    star_list = []
    for i in range(num + 1):
        star = ''
        for _ in range(i):
            star += '*'
        if star != '':
            star_list.append(star)
    for s in star_list:
        print(s)

def print_star_2():
    num = int(input())
    star_list = []
    for i in range(num + 1):
        star = ''
        for _ in range((num) - i):
            star += ' '
        for _ in range(i):
            star += '*'
        if star.replace(' ', '') != '':
            star_list.append(star)
    for s in star_list:
        print(s)

def print_sum():
    list = []

    while (True):
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        else:
            list.append(A + B)
    for i in list:
        print(i)

list = []
for i in range(5):
    A, B = map(int, input().split())
    list.append(A + B)
for i in list:
    print(i)



