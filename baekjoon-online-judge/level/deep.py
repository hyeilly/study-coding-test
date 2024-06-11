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


score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}
all = 0
cnt = 0
while True:
    try:
        subject = list(input().split(" "))
        grade = subject[2]  # 과목평점
        if grade != 'P':
            hj = float(subject[1]) # 학점

            if grade in score:
                all += hj
                cnt += hj * score[grade]
    except:
        print(cnt/all)
        break
