def topToBottom_solution():
    n = int(input())

    array = []
    for i in range(n):
        array.append(int(input()))

    # 파이썬 기본 정렬 라이브러리
    array = sorted(array, reverse=True)

    # 정렬이 수행된 결과 출력
    for i in array:
        print(i, end=' ')

def scoreSort_solution():
    n = int(input())

    array = []
    for i in range(n):
        input_data = input().split()
        # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
        array.append(input_data[0], int(input_data[1]))
    # key를 이용해 점수를 기준으로 정렬
    array = sorted(array, key=lambda student: student[1])

    # 정렬이 수행된 결과를 출력
    for student in array:
        print(student[0], end=' ')

def changeValue_solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 배열 A는 오름차순 정렬 수행
    a.sort()
    # 배열 B는 내림차순 정렬 수행
    b.sort(reverse=True)

    # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
    for i in range(k):
        # A의 원소가 B의 원소보다 작은 경우
        if a[i] < b[i]:
            # 두 원소를 교체
            a[i], b[i] = b[i], a[i]
        else:
            # A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
            break
    print(sum(a))