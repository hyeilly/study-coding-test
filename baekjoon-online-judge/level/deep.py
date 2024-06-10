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
# numb = 2 * N - 1
# max_result = ''
# for k in range(numb):
#     result = ''
#     for j in range(numb):
#         result += '*'
#     print(result)