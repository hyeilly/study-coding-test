# 1번째 줄에 숫자의 개수 N(1<=N<=100)
# 2번째 줄에 숫자 N개 공백없이 주어짐

num = int(input())
n_num = input()
answer = 0
for i in range(num):
    answer += int(n_num[i])
print(answer)