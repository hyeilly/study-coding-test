# 오일러 피 함수 구현하기
# 자연수 n이 주어졌을 때 GCD(n, k) = 1 (=두 수의 최대공약수가 1 =서로소)
# (1<=k<=n)을 만족하는 자연수의 개수를 구하는 프로그램 작성

# 입력 : 1번째 줄에 자연수 n(1<=n<=10^12)
# 출력 : GCD(n,k) = 1(1<=k<=n)을 만족하는 자연수 개수 출력

N = 10
N_list = [(i+1) for i in range(N)]
print(N_list)

for (sdx, s) in enumerate(N_list):
    if s > 1:
        f = s
        while(s <= N):
            if int(s % f) == 0:
                # 배수인 경우
                cal = int(s - (s / f))
                print(f"cal:{cal} s:{s} f:{f}")
                if s in N_list:
                    N_list[N_list.index(s)] = cal
            s += 1
        print("===")
            # cal = int(f - (f / s))
            # print(f"f:{f} s:{s} cal:{cal}")
            # if f in N_list:
            #     N_list[N_list.index(f)] = cal
            # f += s
        #     first = first + s
        #     print(first)
        #     if first in N_list:
        #         N_list.remove(first)
print(N_list)