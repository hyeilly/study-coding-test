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


# N = int(input())
# S = 2 * N - 1
# S_h = int(S / 2)
# S_half = int(S / 2)
# t = 1
# for i in range(S):
#     S_h -= 1
#     star = ''
#     for j in range(abs(S_h+1), 0, -1):
#         star += ' '
#     if i > S_half:
#         print(i)
#
#     else:
#         print(i)
#
#
#     print(star)
# for k in range(1, S):
#     print(k + (k - 1))


# print(i * 3 - 1)


# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = input()
# cnt = 0
# found_count = [x for x in croatia if x in s]
# print(found_count)
# for i in found_count:
#     s = s.replace(i, '')
#     cnt += 1
# cnt += len(list(s))
# print(cnt)
