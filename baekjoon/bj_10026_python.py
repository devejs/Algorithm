"""
10026. 적록색약
210414 Solution
1. bfs를 두 번 돌아야 하므로 인풋 배열 deepcopy
2. 배열 사이즈만큼 돌면서 방문 처리('X')가 안 된 지점에서 bfs 시작, 끝나면 한 구역이 종료되었으므로 cnt++
3. 2번을 적록색약인 경우, 아닌 경우 두번을 돈다
4. bfs 함수에서는 적록색약인지 아닌지 경우와 해당 구역의 색을 받아 큐를 돌기 시작
5. 적록색약이 아닌 경우는 일반적으로 bfs를 돌지만, 적록색약인 경우 R,G의 구분이 없게 하기 위해 딕셔너리 자료구조 사용
6. 딕셔너리는 'B' 값만 0으로 되어 있으므로 해당 값이 조건문에 들어갈 경우 False
7. 따라서 구역의 색깔과 탐색 위치의 색깔이 둘다 True거나 둘다 False일 경우에만 큐에 추가됨
"""
from copy import deepcopy

def bfs(i,j, k, c):
    global n
    q = [(i,j)]
    mapp[k][i][j] = 'X'
    while(len(q)):
        y,x = q.pop(0)
        for dy, dx in move:
            yy = y+dy
            xx = x+dx
            if 0<=yy<n and 0<=xx<n:
                if k == 0 and mapp[k][yy][xx] == c:
                    # R, G, B
                    mapp[k][yy][xx] = 'X'
                    q.append((yy,xx))
                elif k==1 and mapp[k][yy][xx] != 'X':
                    # RG, B
                    if (dic[c] and dic[mapp[k][yy][xx]]) or not (dic[c] or dic[mapp[k][yy][xx]]):
                        mapp[k][yy][xx] = 'X'
                        q.append((yy, xx))


move = [(1,0),(-1,0),(0,1),(0,-1)]
n = int(input())
mapp = [[], []]
ans = [0,0]
for _ in range(n):
    mapp[0].append(list(input()))

mapp[1] = deepcopy(mapp[0])

dic = {'R':1, 'G':2, 'B':0}

for i in range(n):
    for j in range(n):
        if mapp[0][i][j] != 'X':
            bfs(i,j, 0, mapp[0][i][j])
            ans[0] += 1
        if mapp[1][i][j] != 'X':
            bfs(i, j, 1, mapp[1][i][j])
            ans[1] += 1

print(ans[0], ans[1])