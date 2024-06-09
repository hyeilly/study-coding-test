def print_str_idx():
    S = list(input())
    i = int(input())
    print(S[i - 1])

def print_str_len():
    S = list(input())
    print(len(S))

def print_str():
    T = int(input())
    result = []
    for _ in range(T):
        S = input()
        res = ''
        res += S[0] + S[len(S)-1]
        result.append(res)
    for r in result:
        print(r)

def print_ascii():
    A = input()
    print(ord(A))

def sum_int():
    I = int(input())
    S = list(input())
    answer = 0
    try:
        for s in S:
            answer += int(s)
    except:
        pass
    print(answer)

def for_str():
    T = int(input())
    res = []
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        S = list(S)
        result = ''
        for s in S:
            for _ in range(R):
                result += s
        res.append(result)
    for r in res:
        print(r)

def count_word():
    S = list(input().split(' '))
    cnt = 0
    for s in S:
        if s != '':
            cnt += 1
    print(cnt)

def constants():
    numb = list(input().split(' '))
    result = []
    for n in numb:
        n = n[::-1]
        result.append(int(n))
    print(max(result))

# from string import ascii_lowercase
# alpha_list = list(ascii_lowercase)
# alpha_check = list(0 for _ in range(24))
# print(alpha_list)
# S = list(input())
# print(S)

