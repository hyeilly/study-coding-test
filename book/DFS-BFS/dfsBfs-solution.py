from collections import deque

class DfsBfsSolution:
    def __init__(self):
        pass
    def ex1_solution1(self):
        """
        음료수 얼려 먹기
        4 5
        00110
        00011
        11111
        00000
        Returns: 3
        """
        n, m = map(int, input().split())

        # 2차원 리스트의 맵 정보 입력받기
        graph = []
        for i in range(n):
            graph.append(list(map(int, input())))

        # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
        def dfs(x, y):
            # 주어진 범위를 벗어나는 경우에는 즉시 종료
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            # 현재 노드를 아직 방문하지 않았다면
            if graph[x][y] == 0:
                # 해당 노드 방문 처리
                graph[x][y] = 1
                # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
                dfs(x - 1, y)
                dfs(x, y - 1)
                dfs(x + 1, y)
                dfs(x, y + 1)
                return True
            return False

        # 모든 노드(위치)에 대하여 음료수 채우기
        result = 0
        for i in range(n):
            for j in range(m):
                # 현재 위치에서 DFS 수행
                if dfs(i, j) == True:
                    result += 1
        print(result)

    def ex2_solution1(self):
        """
        미로 탈출
        5 6
        101010
        111111
        000001
        111111
        111111
        Returns: 10
        """
        n, m = map(int, input().split())
        graph = []
        for i in range(n):
            graph.append(list(map(int, input())))

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
                    if nx < 0 or ny < 0 or nx >=n or ny >= m:
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
    DfsBfsSolution.ex1_solution1('')
    # DfsBfsSolution.ex2_solution1('')