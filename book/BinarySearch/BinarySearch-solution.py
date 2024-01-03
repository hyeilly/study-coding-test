def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

def exec_binary_search():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    # M(손님이 확인 요청한 부품 개수)
    m = int(input())
    # 손님이 확인 요청한 전체 부품 번호
    x = list(map(int, input().split()))
    # 손님이 확인 요청한 부품 번호 하나씩 확인
    for i in x:
        result = binary_search(array, i, 0, n - 1)
        if result != None:
            print('yes', end = ' ')
        else:
            print('no', end = ' ')

def binary_search_count_sort():
    n = int(input())
    array = [0] * 1000001

    for i in input().split():
        array[int(i)] = 1
    m = int(input())
    x = list(map(int, input().split()))
    for i in x:
        if array[i] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def binary_search_set():
    n = int(input())
    array = set(map(int, input().split()))
    m = int(input())
    x = list(map(int, input().split()))
    for i in x:
        if i in array:
            print('yes', end=' ')
        else:
            print('no', end=' ')