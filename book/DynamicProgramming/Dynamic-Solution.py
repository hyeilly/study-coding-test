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

antWar()