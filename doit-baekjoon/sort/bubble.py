# 3, 2, 1 swap 3번 발생
# 1<=N<=500,000

N = 8 # 수의 개수
A = [3, 2, 8, 1, 7, 4, 5, 6]
# swap이 총 몇 번 발생할 지
cutting = int(N / 2)
front = A[:cutting]
back = A[cutting:]
print(front)
print(back)
index = 0
swap = 0
answer = []

for b in back:
    for fdx, f in enumerate(front):
        print(f"b:{b} 와 f:{f} 비교")
        if f < b:
            answer.append(f)
            swap += 1
            continue
        else:
            answer.append(b)
            swap += fdx
            continue
print(answer)
