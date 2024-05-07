def solution(N, A):
    answer = []
    cursor = 0
    copy = ''
    for i in range(N):
        if 'input' in A[i]:
            answer.insert(cursor,A[i].split('input ')[1])
            cursor += 1
        elif 'move' in A[i]:
            cursor = int(A[i].split('move ')[1])
        elif 'copy' in A[i]:
            cut = A[i].split('copy ')[1]
            cut = cut.split(' ')
            copy = ''.join(answer[int(cut[0]):int(cut[1])])
        elif i == 'paste':
            answer.insert(cursor, copy)
    print("".join(answer))

    return answer

solution(6, ["input a", 'input b', 'input c', 'copy 1 2', 'move 1', 'paste'])