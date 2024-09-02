import re


def print_seed():
    print("         ,r'\"7")
    print("r`-_   ,'  ,/")
    print(" \. \". L_r'")
    print("   `~\/")
    print("      |")
    print("      |")


def chess_calc():
    chess = [1, 1, 2, 2, 2, 8]
    dh = list(map(int, input().split()))
    result = []
    for i in range(len(chess)):
        result.append(chess[i] - dh[i])
    for r in result:
        print(r, end=' ')


def palindrome():
    S = list(input())
    a = ''.join(S)
    b = ''.join(S[::-1])
    if a == b:
        print(1)
    else:
        print(0)


def word_study():
    S = list(input().lower())
    result = {}
    for i in S:
        if i not in result:
            result[i] = 0
        else:
            result[i] += 1
    li = [k for k, v in result.items() if max(result.values()) == v]
    if len(li) > 1:
        print("?")
    else:
        print(li[0].upper())


def your_score():
    score = {
        "A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0
    }

    hj_total = 0
    cnt = 0

    while True:
        try:
            subject, hj, grade = list(input().split(" "))
            hj = float(hj)
            if grade != 'P':
                hj_total += hj
                cnt += hj * score[grade]
        except:
            break
    print('%.6f' % (cnt / hj_total))

def croatia():
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    s = input()
    for i in croatia:
        s = s.replace(i, '*')
    print(len(s))

def star():
    n = int(input())
    for i in range(1, n):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def group_word_checker():
    n = int(input())
    result = n
    for _ in range(n):
        groupWord = []
        word = input()
        for w in word:
            if w not in groupWord:
                groupWord.append(w)
            else:
                if groupWord[len(groupWord)-1] != w:
                    result -= 1
                    break
    print(result)
