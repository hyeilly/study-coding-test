# 큰 수부터 줄여나가야함 - TopDown
def make1(input_data, cnt):
    if input_data == 1:
        return cnt
    else:
        if input_data % 2 == 0:
            # 짝수일 때 1을 빼주어야함.
            input_data -= 1
            cnt += 1
        elif input_data % 5 == 0:
            # 5로 나누어 떨어지면 계산
            input_data /= 5
            cnt += 1
        elif input_data % 3 == 0:
            # 3로 나누어 떨어지면 계산
            input_data /= 3
            cnt += 1
        elif input_data % 2 == 0:
            # 2로 나누어 떨어지면 계산
            input_data /= 2
            cnt += 1
        return make1(input_data, cnt)

print(make1(25, 0))

# BottomUP
