"""
1948. 중간 평균값
210223 Solution
1. 최소, 최대 구해서 반복문
c++로 max,min 함수 쓰지 않고 다시 풀어보기
"""

tc = int(input())
for tc in range(1, tc+1):
    nums = list(map(int, input().split()))
    min_n = min(nums)
    max_n = max(nums)
    summ = 0
    for i in nums:
        if i != min_n and i != max_n:
            summ += i
    ans = round(summ/(len(nums)-2))
    print(f"#{tc} {ans}")