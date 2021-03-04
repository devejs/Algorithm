"""
2115. 벌꿀 채취
210304 Solution
1. 일꾼이 항상 두 명이므로 채취할 수 있는 벌꿀의 최댓값을 구해 가능한 두 개를 배정하기로 함
2. 최댓값을 구할 때, 합이 같더라도 두 값이 다르면 제곱의 합이 달라질 수 있으므로 제곱의 합을 계산해서 저장, 새 배열 생성
3. 새 배열에서 두 개의 최댓값을 구하되, 같은 행에 있을 수도 있으므로 중복 제거가 필요
4. 각 행에서 최댓값을 구하고, 그 최댓값에 대해 중복 가능성이 있는 값들과 최댓값을 제외해준다.
5. 각 행에서 4번의 결과를 제외한 최댓값을 구해준다.
6. 이렇게 구한 각 행의 최댓값과 두번째 최댓값은 중복될 일이 없으므로 정렬해서 가장 큰 두 개의 합이 두 일꾼의 채취 최댓값
"""
from itertools import combinations

def get_max(col, idx, m):
    global emp
    part= hives[col][idx:idx+m]
    max = 0
    for i in range(1,m+1):
        subset = combinations(part, i)
        for st in subset:
            s = sum(st)
            if s <= emp:
                sqr_s = sum([x*x for x in st])
                if sqr_s > max:
                    max = sqr_s
    return max

tc = int(input())
for tc in range(1,tc+1):
    size, hive, emp = map(int, input().split())
    hives = []
    for _ in range(size):
        hives.append(list(map(int,input().split())))
    honey = [[] for _ in range(size)]

    for i in range(size):
        for j in range(size-hive+1):
            honey[i].append(get_max(i, j, hive))

    maxx = [[] for _ in range(size)]
    for index, row in enumerate(honey):
        m = max(row)
        maxx[index].extend([m,0])
        i = row.index(m)
        idx = [i]
        for k in range(1, hive):
            if i+k < size-hive+1:
                idx.append(i+k)
            if i-k >= 0:
                idx.append(i-k)

        for j,v in enumerate(row):
            if not j in idx:
                if v > maxx[index][1]:
                    maxx[index][1] = v

    new_max = sum(maxx, [])
    new_max.sort()
    answer = new_max[-1]+new_max[-2]
    print(f"#{tc} {answer}")