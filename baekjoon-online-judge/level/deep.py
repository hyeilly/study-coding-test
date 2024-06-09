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

