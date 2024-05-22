
def gcd(n, m):
    first = n
    second = m
    while(second != 0):
        cal = first % second
        first = first if first < second else second
        second = cal
        if cal == 0:
            print(first)
            break

# 재귀의 형태로 구현 가능함

# gcd(6, 10) 반례.. 앞에 수가 더 크면 연산 오류
gcd(270, 192)