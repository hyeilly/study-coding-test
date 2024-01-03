# Top-Down
d = [0] * 100

def pibo(x):
    print(f"f({str(x)})", end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

pibo(6)

# Bottom-Up
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# Bottom-Up Dynamic Programming
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])