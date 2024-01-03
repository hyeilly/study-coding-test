def topToBottom_selection():
    """
    위에서 아래로 - 선택정렬
    크기에 상관없이 나열. 큰 수부터 작은 수의 순서로 정렬
    3
    15
    27
    12
    """
    array = list(map(int, input().split()))
    # array = [3, 15, 27, 12]
    # 가장 큰 값 인덱스 가져오기
    # 초기단계 가장 큰 데이터 선택해 맨 앞 데이터와 변경
    # array[0], array[max_idx] = array[max_idx], array[0]
    for i in range(0, len(array)):
        max_idx = array.index(max(array[i:]))
        array[i], array[max_idx] = array[max_idx], array[i]
    print(array)

def topToBottom_module():
    """
    3
    15
    27
    12
    """
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    array.sort(reverse=True)
    for i in array:
        print(i, end=' ')

def scoreSort_insertion():
    """
    성적이 낮은 순서로 학생 출력하기
    3
    홍길동 95
    가나다 22
    이순신 77
    """
    # 학생수
    n = int(input())
    result = []

    for i in range(n):
        # array = []
        data = input().split()
        result.append(tuple(data[0], int(data[1])))
        # result.append(array)
    # 첫번째 데이터는 고정, 두번째 데이터부터 시작
    for r in range(1, len(result)):
        # 뒤에서부터 데이터 비교 시작
        for i in range(r, 0, -1):
            if result[i][1] < result[i - 1][1]:
                result[i], result[i - 1] = result[i - 1], result[i]
            else:
                break
    for i in result:
        print(i[0], end=' ')

        # 비어있는 리스트면 추가
        # if len(result) < 1:
        #     result.append(tuple_)
        # else:
        #     for a in range(len(result), 0 , -1):
        #         if array[tuple_[a]] array[]
            # for (adx, a) in enumerate(result):
            #     target_score = a[1]
            #     score = tuple_[1]
            #     if score < target_score:
            #         result.insert(adx-1, tuple_)
            #     else:
            #         result.append(tuple_)
            #     break


    #     array = tuple(input().split())
    #     array_list.append(array)
    # print(array_list)

def scoreSort_module():
    n = int(input())
    data = []

    for i in range(n):
        array = []
        input_data = input().split()
        array.append(input_data[0])
        array.append(int(input_data[1]))
        tuple_ = tuple(array)
        data.append(tuple_)

    def setting(data):
        return data[1]

    result_ = sorted(data, key=setting)
    print(result_)

def changeArray_module():
    """
    바꿔치기 연산 : 배열 A에 있는 원소 , 배열 B에 있는 원소 골라 2개 원소 서로 바꿈
    배열 A의 모든 원소의 합이 최대가 되도록
    5 3
    1 2 5 4 3
    5 5 6 6 5
    Returns:
    """
    n, k = map(int, input().split())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))

    array1.sort()
    array2.sort(reverse=True)

    for i in range(k):
        array1[i], array2[i] = array2[i], array1[i]
    print(sum(array1))


topToBottom_selection()
# topToBottom_module()
# scoreSort_insertion()
# scoreSort_module()
# changeArray_module()