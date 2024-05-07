
def solution(N, Q, A, S):
    result = []
    print(S)
    for word in S:
        if word[-1] == '?':
            word = word[:-1].lower()
            sub_result = []
            for i, doc in enumerate(A):
                print(f"doc:{doc.lower()} word:{word.lower()}")
                if word.lower() in doc.lower():
                    sub_result.append(i)
            result.append(sub_result)
        else:
            sub_result = []
            for i, doc in enumerate(A):
                if word in doc:
                    sub_result.append(i)
            result.append(sub_result)
    return result

solution(4, 3, ["WWW stands for world wide web", "for no contents", "", "www internet four fo r"], ["WWW", "Www?", "for"])