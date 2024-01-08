# 2. 1로 만들기
# X가 5로 나누어떨어지면, 5로 나눔
# X가 3로 나누어떨어지면, 3로 나눔
# X가 2로 나누어떨어지면, 2로 나눔
# X에서 1을 뺀다
# 첫째 줄에 정수 X 주어짐 (1<=x<=30000)

x = 26
# 1부터 30000까지
d = [0] * (x+1)
# f(2)
for i in range(2, x+1):
    # BottomUp 이므로 X에서 1을 빼는 것부터 시작
    # 앞에 숫자에 +1하면 8일 경우 => 1을 뺀 7

    d[i] =d[i - 1] + 1
    if i % 2 == 0:
        # 더 값이 작은 것이 있다면 update
        # 자기 자신을 찾기 위한 d[i//2] + 1
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])