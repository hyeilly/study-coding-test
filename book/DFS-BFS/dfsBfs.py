from collections import deque
class DfsBfs:
    def __init__(self):
        pass

    def ex1(self):
        """
        N X M 크기의 얼음틀. 구멍 뚫린 부분은 0, 칸막이 존재하는 부분은 1
        구멍 뚫린 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
        """
        result = 0
        ice = [
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        # ice[0][0]의 연결 ice[0][1] ice[1][0]
        stack = []
        # 최상단 행열 저장
        stack.append([0, 0])
        # 인접노드 가까운 것 먼저 저장
        stack.append([0, 1])
        # ice[0][1]의 연결 ice[0][0]  ice[1][1] 1인 것인 ice[0][2]는 제외
        stack.append([1, 1])
        # ice[1][1]의 연결 ice[0][1] ice[1][0] ice[1][2] 1인 것인 ice[2][1]는 제외
        stack.append([1, 0])
        # ice[1][0]의 연결 ice[0][0] ice[1][1] 1인 것인 ice[2][0]
        stack.remove([0, 0])
        ice[0][0] = 1
        # ice[1][1] 의 연결 ice[1][2]
        stack.append([1, 2])
        # ice[1][2]의 연결 1인 ice[0][2] ice[1][3] ice[1][1] ice[2][2]
        # 인접노드 모두 1이므로 제거
        stack.remove([1, 2])
        ice[1][2] = 1
        # 다음 ice[1][0]의 연결이었던 ice[0][0]은 이미 1이 되었음, ice[1][1]
        stack.remove([1,1])
        ice[1][1] = 1
        # 다음 ice[1][1]의 연결이었던 ice[1][0]
        stack.remove([1, 0])
        ice[1][0] = 1
        # 다음 ice[1][1]의 연결이었던 ice[0][1]
        stack.remove([0,1])
        ice[0][1] = 1

        print(stack)
        print(ice)
        result += 1

        # 나온 결과값으로 다시 0찾기
        # ice[0][4]의 연결 ice[0][3], ice[1][4]는 둘다 1
        stack.append([0,4])
        # 인접노드 없어 스택에서 꺼내기
        stack.remove([0,4])
        ice[0][4] = 1
        print(stack)
        print(ice)
        result += 1

        # 다음 0위치 찾기
        # ice[3][0]의 연결 ice[3][1] 1인 ice[2][0]은 제외
        stack.append([3, 0])
        # 인접노드 ice[3][1] 저장
        stack.append([3, 1])
        # ice[3][1]의 인접노드 ice[3][2] 1인 ice[2][1] 이미 stack에 존재하는 ice[3][0]
        stack.append([3, 2])
        # ice[3][2]의 인접노드 ice[3][3] 1인 ice[2][2] 이미 stack에 존재하는 ice[3][1]
        stack.append([3, 3])
        # ice[3][3]의 인접노드 ice[3][4] 1인 ice[2][3] 이미 stack에 존재하는 ice[3][2]
        stack.append([3, 4])
        # ice[3][4]의 인접노드 1인 ice[2][4]밖에 없어 remove
        stack.remove([3, 4])
        ice[3][4] = 1
        # ice[3][3]의 인접노드 없음
        stack.remove([3, 3])
        ice[3][3] = 1
        stack.remove([3, 2])
        ice[3][2] = 1
        stack.remove([3, 1])
        ice[3][1] = 1
        stack.remove([3, 0])
        ice[3][0] = 1
        print(stack)
        print(ice)
        result += 1
        print(result)

    def ex2(self):
        """
        N X M 크기 직사각형 형태 미로
        미로에는 여러 마리 괴물이 있어 피해 탈출. 동빈 위치는 (1, 1)  출구는 (N, M)
        괴물이 있는 부분은 0, 괴물이 없는 부분은 1
        인덱스는 1, 1으로 시작
        """
        n, m = 5, 6
        ice = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        cnt = 0
        queue = deque()
        # 시작노드 ice[1][1]
        queue.append([1, 1])
        # 꺼내고 인접노드 ice[2][1]  0은 괴물이 있음
        ice[0][0] = 2
        queue.remove([1, 1])
        cnt += 1
        queue.append([2, 1])
        print(queue)
        # 꺼내고 인접노드 ice[2][2] 0은 괴물 있음 ice[3][1] 이미 다녀온 ice[1][1]
        ice[1][0] = 2
        queue.remove(queue[0])
        queue.append([2, 2])
        # 꺼내고 인접노드 ice[2][3] 0은 괴물 있음
        print(queue)
        print(ice)

    def ex1_solve(self):
        """
        1 특정한 지점의 상,하,좌,우를 살펴본 뒤 주변 지점 중에서 값이 '0'
          이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
        2 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문 다시 진행

        return 이 9가 나옴...
        """
        n, m = 4, 5
        graph = [
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        stack = []

        def check_ewsn(x, y, type):
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            if type == 'east':
                if (graph[x][y + 1] == 0):
                    return [x, y + 1]

            elif type == 'west':
                if (graph[x][y - 1] == 0):
                    return [x, y-1]
            elif type == 'south':
                if(graph[x + 1][y] == 0):
                    return [x+1, y]
            elif type == 'north':
                if(graph[x - 1][y] == 0):
                    return [x-1, y]


        def dfs_func(x, y):
            result_arr = [[x, y]]
            print(x, y)
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            for i in result_arr:
                x = i[0]
                y = i[1]
                if graph[x][y] == 0:
                    print(f"{x},{y}과 연결된 노드 ")
                    east = check_ewsn(x, y, 'east')
                    west = check_ewsn(x, y, 'west')
                    south = check_ewsn(x, y, 'south')
                    north = check_ewsn(x, y, 'north')
                    print(east)
                    print(west)
                    print(south)
                    print(north)
                return False
        result = 0
        for i in range(n):
            for j in range(m):
                if dfs_func(i, j) == True:
                    result += 1
        print(result)
        print(stack)
    def ex2_solve(self):
        n, m = 5, 6
        graph = [
            [1,0,1,0,1,0],
            [1,1,1,1,1,1],
            [0,0,0,0,0,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
        ]
        # 이동할 네 방향 정의 (상, 하, 좌, 우)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # BFS 소스코드 구현
        def bfs(x, y):
            # 큐(Queue) 구현을 위해 deque 라이브러리 사용
            queue = deque()
            queue.append((x, y))
            # 큐가 빌 때까지 반복
            while queue:
                x, y = queue.popleft()
                # 현재 위치에서 네 방향으로의 위치 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 미로 찾기 공간을 벗어난 경우 무시
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    # 벽인 경우 무시
                    if graph[nx][ny] == 0:
                        continue
                    # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
            # 가장 오른쪽 아래까지의 최단 거리 반환
            return graph[n - 1][m - 1]

        # BFS를 수행한 결과 출력
        print(bfs(0, 0))



if __name__ == '__main__':
    # DfsBfs.ex2('')
    # DfsBfs.ex1('')
    DfsBfs.ex1_solve('')
    # DfsBfs.ex2_solve('')