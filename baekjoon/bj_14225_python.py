"""
14225. 부분 수열의 합
210324 Solution
전형적인 조합 문제(부분집합)
1. 부분집합의 개수에 따른 합 리스트 구하기
2. 숫자 증가시켜가면서 1번 리스트에 값이 없으면 만들 수 없는 최소 자연수이므로 break
3. 모든 자연수가 다 있을 경우 그 자연수보다 큰 수이므로 1 증가된 수(num) 출력하면 됨
"""
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
num = 1
numbers = set()
for i in range(1,n+1):
    for tup in list(combinations(arr, i)):
        numbers.add(sum(tup))
numbers = list(numbers)
numbers.sort()
for i in numbers:
    if i == num:
        num += 1
    else:
        break
print(num)

"""
처음에는 정렬해서 그리디로 풀어볼까 했는데 수열 크기 20이면 할 만 한가..? 한번 도전은 해 보기
콤비네이션 라이브러리 안 쓰면 시간 차이 얼마나 나는지 보기

"""