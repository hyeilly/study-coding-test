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
        queue.remove([1, 1])
        cnt += 1
        queue.append([2, 1])
        print(queue)
        # 꺼내고 인접노드 ice[2][0] ice[2][2]



if __name__ == '__main__':
    DfsBfs.ex2('')
    # DfsBfs.ex1('')