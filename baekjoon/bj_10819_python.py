"""
10819. 차이를 최대로
210406 Solution 
1. dfs로 완전탐색
"""
def dfs(d, v, sum):
    global num, result
    if d == num-1:
        if result < sum:
            result = sum
        return
    for i in range(num):
        if not checked[i]:
            checked[i] = 1
            dfs(d+1, arr[i], sum+abs(arr[i]-v))
            checked[i] = 0

num = int(input())
arr = list(map(int, input().split()))
checked = [0 for _ in range(num)]
result = 0
for i in range(num):
    checked[i] = 1
    dfs(0, arr[i], 0)
    checked[i] = 0
print(result)