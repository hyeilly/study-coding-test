# 트리 순회하기
# 전위 순회 ABDCEFG(루트)(왼쪽)(오른쪽)
# 중위 순회 DBAECFG(왼쪽)(루트)(오른쪽)
# 후위 순회 DBEGFCA(왼쪽)(오른쪽)(루트)

# 입력
# 1번째 줄에 이진 트리 노드개수 N(1<=N<=26)
# 2번째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드 주어짐
# 노드의 이름은 A부터 차례대로 영문자, 대문자, 항상 A가 루트 노드
# 자식 노드 없을 때는 . 으로 표현

N = 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
input_data = [
    ['A', 'B', 'C'],
    ['B', 'D', '.'],
    ['C', 'E', 'F'],
    ['E', '.', '.'],
    ['F', '.', 'G'],
    ['D', '.', '.'],
    ['G', '.', '.'],
]
aList = []
result = []
def preOrder(now):
    idx = aList.index(now)
    if len(front[idx]) > 1:
        left, right = front[idx]
    else:
        left = front[idx][0]
        right = 0

    if type(left) != int:
        result.append(left)
    if left == -1 or right == -1:
        return result
    preOrder(left)
    if type(right) != int:
        result.append(right)
    preOrder(right)

def inOrder(now):
    pass

def postOrder(now):
    pass


# 전위 순회
front = []
for idx, i in enumerate(input_data):
    node, left, right = i
    aList.append(node)
    inp = []
    if left != '.':
        inp.append(left)
    if right != '.':
        inp.append(right)
    if left == '.' or right == '.':
        inp.append(-1)
    front.append(inp)
result.append('A')
preOrder('A')
answer = ''.join(result)
print(answer)






