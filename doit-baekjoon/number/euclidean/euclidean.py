
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

gcd(270, 192)