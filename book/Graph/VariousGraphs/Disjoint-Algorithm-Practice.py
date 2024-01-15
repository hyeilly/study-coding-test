
V = 6

tree = [idx for idx in range(1, V+1)]
# 부모에 대한 정보 담기
parent = [t for t in tree]

# step1
union = (1, 4)
find_min = 0
for u in union:
    # 루트노드에서 찾아야함
    if u in parent:
        idx = parent.index(u)
        print(idx)
print(parent)


