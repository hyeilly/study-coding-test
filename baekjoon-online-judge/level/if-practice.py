
# A, B = map(int, input().split())
A, B = 1, 2

if A > B: print('>')
elif A < B: print('<')
elif A == B: print('==')

# score = int(input())
score = 89
if 90 <= score <= 100: print('A')
elif 80 <= score <= 89: print('B')
elif 70 <= score <= 79: print('C')
elif 60 <= score <= 69: print('D')
else: print('F')

def leaf_year():
    year = int(input())

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(1)
    else:
        print(0)

# leaf_year()

def coordinate():
    A = int(input())
    B = int(input())
    if(A > 0 and B > 0): print(1)
    elif(A < 0 and B > 0): print(2)
    elif(A < 0 and B < 0): print(3)
    else: print(4)

# coordinate()

def alarm():
    H, M = map(int, input().split())

    if M < 45:
        M = M + 60 - 45
        H -= 1
    else:
        M -= 45
    if H < 0:
        H += 24


    print(H, M)

# alarm()
def make_oven():
    H, M = map(int, input().split())
    timer = int(input())
    M += timer
    if M > 59:
        H += M // 60
        M = M % 60
    if H > 23:
        H = int(H % 24)
    print(f"{H}:{M}")


# make_oven()
def dice_game():
    r1, r2, r3 = map(int, input().split())
    li = [r1, r2, r3]
    if r1 == r2 == r3:
        print(10000 + r1 * 1000)
    elif r1 == r2 or r1 == r3 or r2 == r3:
        if r1 == r2 or r1 == r3:
            print(1000 + r1 * 100)
        else:
            print(1000 + r2 * 100)
    else:
        print(max(li) * 100)

dice_game()
3