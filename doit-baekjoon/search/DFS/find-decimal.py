# 7331 소수
# 왼쪽 부터 4자리수 모두 소수
# 숫자 N이 주어졌을 때 N자리 숫자 중 신기한 소수
# DFS 완전탐색해도 문제 없을 조건이 주어짐 => N(1<=N<=8)
# 소수를 판별하는 방법으로 보통 에라토스테네스의 체를 사용하지만
# 여기서는 단순한 소수 판별 함수 사용해서 풀기 가능

N = 4

decimal = [2, 3, 5, 7]
# 4, 6, 8 9는 소수가 아니므로 제외
exp = [4, 6, 8, 9]

my_stack = []
answer = []

index = 0
while (index != len(decimal)):
    print('fff')

    index += 1
