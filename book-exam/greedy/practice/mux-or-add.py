s = input()
limit = 2000000000
result = 1
idx = 0
while True:
    numb = int(s[idx])
    if numb == 0:
        result = 0
        idx += 1
        numb = int(s[idx])
        result += numb
        idx += 1
        print(f"if - idx:{idx} numb:{numb}")
    else:
        numb = int(s[idx])
        result *= numb
        idx += 1
        print(f"else - idx:{idx} numb:{numb}")
    if idx == len(s):
        break

print(result)