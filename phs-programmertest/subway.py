# 지하철 노선 N개 역
# 각 역은 1번부터 N번까지 번호. 지하철 열차 1 번 ~ 모든 역 정차 N번까지
# 최대 C명 사람 태울 수 있음.
# N번 역 제외 각 역에는 몇 명 사람들 열차 기다림
# 모두 지하철 타고 마지막 N 번 역까지 갈 것
# 1번 역에서 X대의 열차 출발. 열차 기다리고 있는 사람들은 열차 꽉 차있지 않으면 열차 탑승
# N : 노선에 있는 역의 개수
# C : 열차 하나에 탈 수 있는 사람의 수
# X : 열차의 댓수
# A : A[i] i+1번 역에서 기다리고 있는 사람의 수

def solution(N, C, X, A):
    answer = []
    train = [ 0 for i in range(X) ]
    print(train)
    for i in range(N-1):
        print(f"다음역 도착 {i+1} {A[i]}명 태우기")
        for t in range(len(train)):
            if train[t] <= C:
                train[t] += A[i]
                # 넘어가
                break
        print(train)




solution(4, 10, 6, [10, 30, 25])
