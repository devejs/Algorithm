"""
11659. 구간 합 구하기 4
210512 Solution
1. 각 자릿수까지의 합을 구한다.
2. [i,j]인 구간의 합은 J까지의 합에서 i-1까지의 합을 뺀 값
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = []
dp.append(lst[0])
for i in range(1,n):
    dp.append(dp[i-1]+lst[i])
for _ in range(m):
    i,j = map(int, input().split())
    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])