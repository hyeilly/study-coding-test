- 점화식 : 수열의 일반항을 한 개 이상의 앞전항 이용해서 나타낸 식
# 조합
- nCr 으로 표현 : n개의 숫자에서 r개를 뽑는 경우의 수
- 조합과 비교되는 순열 nPr으로 표현 : n개의 숫자 중 r개를 뽑는 순서를 고려해 나열할 경우의 수
- 조합에서는 1, 2, 3 과 3, 2, 1 은 같다고 보지만 순열에서는 다른 경우로 판단

## 순열과 조합의 핵심 이론
- 순열
  - nPr = n! / (n - r)!
- 조합
  - nCr = n! / (n - r)!r!
  - r!은 순서가 다른 경우의 수를 제거하는 역할
  - 조합은 순서를 고려하지 않으므로
# 알고리즘 관점
1. 특정 문제를 가정하기
- 5개의 데이터에서 3개 선택 [1, 2, 3, 4, 5]
2. 모든 부분 문제가 해결된 상황이라고 가정하고 지금 문제 생각
- 자기 자신과 관계된 함수를 가지고 문제 해결
- 5개 데이터 중 3개를 뽑아야함. 
- 이미 선택이 완료된 데이터로 가정해서 [1, 2, 3, 4] 이건 끝
- 마지막 5
  - 선택함 : 선택이 완료된 데이터 중 2개를 선택하는 경우의 수
  - 선택 안함 : 선택이 완료된 데이터 중 3개를 선택하는 경우의 수 
  - 선택함 + 선택 안함 => 5개 중 3개를 선택하는 경우의 수
- 5C3 만들 수 있는 케이스는 4C2와 4C3 => 5C3 = 4C3 + 4C2
- 5개중 3개를 선택하는 경우의 수 점화식
  - D\[5][3] = D\[4][2] + D\[4][3]
3. 특정 문제를 해결한 내용을 바탕으로 일반 점화식 도출 
- 조합 점화식
  - D\[i][j] = D\[i - 1][j] + D\[i - 1][j - 1]