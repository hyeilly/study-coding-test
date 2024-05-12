# 문제푸는 순서
# 1. 스택 채워져 있거나 A[index] > A[top]인 경우 pop 인덱스 이용해 정답 수욜이 오큰수 저장
# pop은 조건을 만족하는 동안 계속 반복
# 2. 현재 인덱스를 스택에 push 하고 다음 인덱스로 넘어감
# 3. 수열 길이만큼 반복한 다음 현재 스택에 남아있는 인덱스에 -1 저장

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    # 현재 스택의 top에 있는 값
    while myStack and A[myStack[-1]] < A[i] : # 오큰수 조건
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ''
for i in range(n):
    result += str(ans[i]) + ' '
print(result)