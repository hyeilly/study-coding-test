# p313
# 0~9로 이루어진 문자열 S
# 왼쪽부터 오른쪽으로 하나씩 확인 => x 혹은 + 연산

# s = '02984'
s = '567'
s_list = list(map(int, s))
i = 0
result = 1
while True:
    if s_list[i] == 0 and i == 0:
        i += 1
        result += s_list[i] - 1
        i += 1
        print(result)
    else:
        result *= s_list[i]
        print(f"s_list:{s_list[i]} i:{i} result:{result}")
        i += 1
        if i == len(s_list):
            break
print(result)