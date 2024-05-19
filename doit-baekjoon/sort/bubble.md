# 버블 정렬 과정
1. 비교 연산이 필요한 루프 범위 설정
2. 인접한 데이터 값 비교
3. swap 조건 부합하면 swap 연산 수행
4. 루프 범위 끝날 때까지 2~3 반복
5. 정렬 영역을 설정. 다음 루프를 실행할 때는 이 영역 제외
6. 비교 대상이 없을 때까지 1~5 반복

특정한 루프 전체 영역에서 swap이 한 번도 발생하지 않았다면 그 영역 뒤에 있는 데이터가 모두 정렬됐다는 뜻으로 프로세스 종료OK