class DfsBfs:
    def __init__(self):
        pass

    def ex1(self):
        """
        N X M 크기의 얼음틀. 구멍 뚫린 부분은 0, 칸막이 존재하는 부분은 1
        구멍 뚫린 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
        """
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
        # ice[0][1]의 연결 ice[0][0] ice[0][2] ice[1][1]
        stack.append([0, 2])
        # ice[0][2]의 연결 ice[0][1] ice[0][3] ice[1][2]

        print(stack)
        print()
        print()


if __name__ == '__main__':
    DfsBfs.ex1('')