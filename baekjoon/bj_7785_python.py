"""
7785. 회사에 있는 사람
210331 Solution
1. 이름에 중복이 없으므로 동일한 이름이 나올 때마다 딕셔너리의 값 ++
2. 딕셔너리 값이 홀수일 경우 회사에 있음
"""
n = int(input())
dic = {}
names = []
for _ in range(n):
    name, state= input().split()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
for n, s in dic.items():
    if s%2 == 1:
        names.append(n)
names.sort(reverse=True)
for n in names:
    print(n) 
