"""
11399. ATM
210409 Solution
1. 시간은 누적되므로 짧은 시간이 앞으로 갈수록 전체 소요 시간이 짧아짐
2. 정렬된 시간은 n, n-1, n-2, .. 만큼 반복 누적됨(남은 사람의 수만큼)
3. 반복문으로 0~n-1까지 돌릴거기때문에 내림차순(reverse)으로 정렬 후 반복문에서 합
"""
num = int(input())
times = list(map(int, input().split()))
times.sort(reverse = True)
sum = 0
for i in range(num):
    sum += times[i]*(i+1)
print(sum)