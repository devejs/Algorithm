"""
10773. 제로
210426 Solution
1. 0이면 리스트에서 팝(0일때 뺄 것이 있음이 보장됨)
2. 0이 아니면 sum을 더하고 리스트에 append
"""
k= int(input())
sum = 0
num = []
for _ in range(k):
    n = int(input())
    if n == 0:
        sum -= num.pop()
    else:
        sum += n
        num.append(n)
print(sum)