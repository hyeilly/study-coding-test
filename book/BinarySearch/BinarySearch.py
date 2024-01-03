def find_set():
    N = 5
    M = 3
    # 가게의 부품
    n_list = [8, 3, 7, 9, 2]
    # 손님의 부품
    m_list = [5, 7, 9]

    for i in m_list:
        if i in n_list:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def find():
    def find_recursive(array, find_data, start_idx, end_idx):
        while start_idx <= end_idx:
            # 중간점 인덱스 찾기 => 중간점을 기준으로
            mid = (start_idx + end_idx) // 2
            if array[mid] == find_data:
                return mid
            # 중간점 7과 5 비교
            elif array[mid] > find_data:
                # 끝점을 중간점 한칸 앞으로 당겨오기
                end_idx = mid - 1
            else:
                start_idx = mid + 1
        return None

    N = 5
    M = 3
    n_list = [8, 3, 7, 9, 2]
    # 찾아야할 데이터
    m_list = [5, 7, 9]
    n_list.sort()

    for m in m_list:
        result = find_recursive(n_list, m, 0, N - 1)
        if result != None:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def make_ricecake():
    # n : 첫째 줄 떡의 개수
    # m : 떡의 길이
    n, m = 4, 6
    rc = [19, 15, 10, 17]
    start = 0
    end = max(rc)
    mid = end // 2
    cutting_sum = 0
    result = 0
    # 자른 후 떡의 길이가 m보다 길면 시작점 이동
    # for i in range(len(rc)):
    #     if (rc[i] - mid) > 0:
    #         cutting_sum += rc[i] - mid
    #         if cutting_sum > m:
    #             start = mid + 1
    #         elif cutting_sum < m:
    #             end = mid - 1
    # print(f"mid:{mid} cutting 전 :{cutting_sum}")
    while(start<=end):
        cutting_sum = 0
        # 중간값 확인
        mid = (start + end) // 2
        # cut 했을 때 개수 세기
        for i in range(len(rc)):
            if rc[i] - mid > 0:
                cutting_sum += (rc[i] - mid)
        print(f"start : {start}, end: {end}, mid:{mid}, sum:{cutting_sum}")
        if cutting_sum > m:
            start = mid + 1
            continue
        else:
            print(f"start:{start}, end:{end}, mid: {mid}")
            end = mid - 1
            print(end)
            result = end - 1
        break
        # break
        # for i in range()
        # if cutting_sum > m:
        #     cutting_sum = 0
        #     start = mid + 1
        #     mid = (start + end) // 2
        #     for i in range(len(rc)):
        #         if (rc[i] - mid) > 0:
        #             cutting_sum += rc[i] - mid
        #     print(f"mid:{mid} cutting 전 :{cutting_sum}")
        # elif cutting_sum < m:
        #     end = mid - 1
        #     print(end)
        #     if start <= end:
        #         result = start
        # break
    print(result)


# find()
make_ricecake()
