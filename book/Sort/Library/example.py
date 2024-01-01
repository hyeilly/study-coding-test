# sorted()
# 퀵 정렬 동작 방식이 비슷한 병합 정렬 기반으로 만들어짐
# 병합 졍렬은 일반적으로 퀵 정렬보다 느림
# 최악의 경우에도 O(NlogN) 보장

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)
# 리스트 변수 하나 있을 때 내부 원소 바로 정렬 가능

# sort()
# 리스트 객체 내장 함수
# 별도의 정렬된 리스트가 반환되지 않고 내부 원소 바로 정렬
array.sort()
print(array)

# key 매개변수를 입력으로 받을 수 있음
# key 값으로는 하나의 함수가 들어가야 하며 이것이 정려려 기준이 됨
array_ = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]
result_ = sorted(array_, key=setting)
print(result_)

# 정렬 라이브러리의 시간 복잡도
# O(NlogN)
# 단순 정렬을 해야한다면 기본 정렬 라이브러리 사용
# 데이터 범위 한정되어 있으며 빠르게 동작해야한다면 계수 정렬
# 1. 정렬 라이브러리로 풀 수 있는 문제
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제 : 선택/삽입/퀵 정렬 원리
# 3. 더 빠른 정렬 필요한 문제 : 퀵 정렬 기반 기법으로는 풀 수 없음. 계수 정렬 등 다른 정렬 알고리즘 사용