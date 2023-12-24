def sugar_snack():
    # h, w = 5, 5
    # n = 1
    # l, d, x, y = 2, 0, 1, 1
    # 격자판의 세로 가로
    h, w = map(int, input().split())
    data = [[0 for i in range(h)] for j in range(w)]
    # 막대의 개수
    n = int(input())

    # 막대의 길이(l), 방향(d)-가로는 0 세로는 1, 좌표(x, y)
    for i in range(n):
        l, d, x, y = map(int, input().split())
        for j in range(l):
            if d == 0:
                data[x - 1][y - 1 + j] = 1
            else:
                data[x - 1 + j][y - 1] = 1
    for a, b, c, d, e in data:
        print(a, b, c, d, e)

def ants():
    # 갈 수 있는 곳 0, 벽 또는 장애물 1, 먹이 2, 미로 상자의 테두리 모두 벽 (2,2) 에서 출발
    # 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직임
    # 입력 받을때마다 처리하고싶은데...
    pan = []
    for i in range(10):
        pan_det = list(map(int, input().split()))
        pan.append(pan_det)

    x, y = 1, 1
    while x < len(pan):
        for i in range(len(pan[x])):
            if pan[x][y] == 0:
                # 오른쪽 먼저 체크
                pan[x][y] = 9
                y += 1
            elif pan[x][y] == 1:
                x += 1
                y -= 1
                break
        if pan[x][y] == 2:
            pan[x][y] = 9
            break
    # print(pan)
    for p in pan:
        for (jdx, j) in enumerate(p):
            if jdx < len(p)-1:
                print(j, end=' ')
            else:
                print(str(j))


# sugar_snack()
ants()