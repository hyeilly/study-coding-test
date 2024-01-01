N = 10
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 두번째 데이터부터 시작
for i in range(1, N):
    for j in range(i, 0, -1):
        if array[i] < array[j]:

            print(j)
    # if array[i - 1] > array[i]:
    #     temp = array[i]
    #     array[i] = array[i - 1]
    #     array[i - 1] = temp
    #
    #     print(array)
