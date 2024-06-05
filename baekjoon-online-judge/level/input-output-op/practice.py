# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# print(A + B)
# print(A - B)
# print(A * B)
# print(A / B)
# print(A % B)
#
# str = input()
# print(str+"??!")

def change_year():
    year = int(input())
    return year-543

def print_cat():
    print("\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \(__)|")

def print_dog():
    print("|\_/|")
    print("|q p|   /}")
    print("( 0 )\"\"\"\\")
    print("|\"^\"`    |")
    print("||_/=\\\\__|")

A = 472
B = 385
# A = int(input())
A_list = list(map(int,str(A)))
# B = int(input())
B_list = list(map(int, str(B)))
result = 0
rr_ = 1
for b in range(len(B_list)-1, -1, -1):
    r = 0
    r_ = 1
    for a in range(len(A_list)-1, -1, -1):
        r += (B_list[b] * A_list[a] * r_)
        r_ *= 10
    print(r)
    r *= rr_
    rr_ *= 10
    result += r
print(result)


# A, B, C = map(int, input().split())
# print(A + B + C)

