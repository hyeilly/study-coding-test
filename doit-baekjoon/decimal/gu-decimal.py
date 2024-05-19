# 소수의 N 제곱일 때 이 수를 거의 소수
# A와 B 주어질 때 A보다 크거나 같고 B보다 작거나 같은 거의 소수
# 1번째 줄에 왼쪽 범위 A와 오른쪽 범위 B가 공백을 한 칸 사이에 두고 주어짐
# A는 10^14 보다 작거나 같은 자연수
# B는 A보다 크거나 같고 10^14보다 작거나 같음
# N 제곱한 값을 구하는 도중 값이 변수 표현 범위를 초과하는 경우 발생할 수 있음
# 계산 오류 방지를 위해 N^k 과 B 값이 아니라 N과 B / N^k-1 을 비교하는 병식으로 식을 적절하게 정리
# N < B/(N^(k-1))

A, B = 1, 1000
list = [i for i in range(A, B+1, 1)]

for (ldx, l) in enumerate(list):
    if l > 1:
        for i in range(l+l, B+1, l):
            if i in list:
                list.remove(i)
    else:
        list.remove(l)
print(list)
answer = []
for i in list:
    cal = i
    for d in range(i, B+1, i):
        cal = cal * i
        if cal < 1000 and cal not in answer:
            answer.append(cal)

print(answer)
print(len(answer))






# 문제 분석
# 1. 모든 소수를 구해놓고 이 소수들의 N제곱값이 입력된 A와 B 사이에 존재하는지 판단해 문제 해결
# 2. 입력에서 주어진 범위의 최댓값 10^14의 제곱근 10^7 까지 소수 탐색
# N제곱값이 A ~ B범위 안에 존재하는지 판별해 유효한 소수의 개수를 세어 해결