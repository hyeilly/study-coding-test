
# N개 문서, i번 문서 내용은 문자열 A[i]
# 모든 문서의 내용은 알파벳과 공백으로만 이루어짐
# 사용자 특정 단어 검색하면 그 단어 정확하게 등장하는 문서 모두 찾기
# 사용자 검색한 단어 끝에 물음표 있다면 대소문자
# N 인터넷 상 문서 개수
# Q 사용자가 검색한 단어 개수
# A i번 문서의 내용 A[i]
# S i번째로 사용자가 검색한 단어 S[i]

def solution(N, Q, A, S):
    answer = []
    for i in range(Q):
        user_search = S[i]
        answer_index = []
        for j in range(N):
            docs_list = A[j]
            if "?" == user_search.strip()[-1]:
                user_search = user_search.replace('?','').lower()
                docs_list = docs_list.lower()

            if user_search in docs_list:
                answer_index.append(j)
        answer_index.sort()
        answer.append(answer_index)
    print(answer)



    return answer

solution(4, 3, ["WWW stands for world wide web", "for no contents", "", "www internet four fo r"], ["WWW", "Www?", "for"])