# 최소공배수 구하기

# 두 자연수 A와 B가 있을 때 A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수
# A * B / 최대 공약수
# ex) 36 48 => 2 * 2 * 3 * 3 * 4 => 36 = 2 * 2 * 3 * 3 , 48 = 2 * 2 * 3 * 4
# 여기서 2 * 2 * 3 을 빼야함
# 문제분석
# 유클리드 호제법 이용해 최대 공약수 구한 후 두수의 곱에서 최대 공약수를 나눠주는 것으로 해결


t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(t):
    a, b = map(int, input().split())
    result = a * b // gcd(a, b)
    print(result)