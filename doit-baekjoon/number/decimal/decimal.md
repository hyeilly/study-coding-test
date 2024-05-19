# 소수
- 1과 자기 자신 외에 약수가 존재하지 않는 수

# 에라토스테네스의 체 원리 
1. 구하고자 하는 소수의 범위만큼 1차원 배열 생성
2. 2부터 시작하고 현재 숫자가 지워지지 않을 때는 현재 선택된 숫자의 배수에 해당하는 수를 배열에서 끝까지 탐색하면서 지우기.
- 이때 처음으로 선택된 숫자는 지우지 않음(=>이것이 소수)
3. 배열에서 끝까지 2를 반복한 후 배열에서 남아 있는 모든 수를 출럭

# 에라토스테네스의 체 사용 시 시간 복잡도
- O(Nlog(logN))
- 배수를 삭제하는 연산으로 실제 구현에서 바깥쪽 for문 생략하는 경우 빈번하게 발생