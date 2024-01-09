def make1():
    """
    1로 만들기
    정수 X 주어질 때 정수 X 에 사용할 수 있는 연산 4가지
    1. X가 5로 나누어떨어지면, 5로 나눔
    2. X가 3로 나누어떨어지면, 3으로 나눔
    3. X가 2로 나누어떨어지면, 2로 나눔
    4. X에서 1을 빼기
    input = 26 => output = 3
    """
    x = int(input())
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 30001

    # Dynamic Programming Bottom-Up
    for i in range(2, x + 1):
        # 현재 수에서 1을 빼는 경우
        d[i] = d[i - 1] + 1
        # 현재 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        # 현재 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        # 현재 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5]+ 1)

    print(d[x])

def antWar():
    """
    개미 전사 : 최소 한 칸 이상 떨어진 식량창고를 약탈해야함
    N 식량창고 개수
    array 식량창고에 저장된 식량의 개수 K개
    input => output 8
    """
    n = 4
    array = [1, 3, 1, 5]
    # n = int(input())
    # array = list(map(int, input().split()))
    # DP 테이블 초기화
    d = [0] * 100
    # BottomUp
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    # 계산된 결과 출력
    print(d[n-1])

def construction():
    n = int(input())
    d = [0] * 1001

    d[1] = 1
    d[2] = 3
    # BottomUp
    for i in range(3, n + 1):
        d[i] = d[i - 1] + 2 * d[i - 2] % 796796
    print(d[n])

def efficientMoney():
    n, m = map(int, input().split())
    array = []
    # 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수
    # 금액 i => 만들 수 있는 최소한의 화폐 개수를 ai, 화폐 단위 k
    for i in range(n):
        array.append(int(input()))

    d = [1001] * (m + 1)

    # BottomUp
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m + 1):
            # (i - k)원을 만드는 방법이 존재하는 경우
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array[i]] + 1)
    # 계산된 결과 출력
    # 최종적으로 M원을 만드는 방법이 없는 경우
    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])
efficientMoney()