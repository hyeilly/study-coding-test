# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
s = '0001100'
res = ''
count = 0
type = s[0]
for i in range(1, len(s)):
    if type != s[i]:
        print(s[:i])
        break