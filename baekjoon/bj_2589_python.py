"""
2589. 보물섬
210331 Solution
1. bfs, 최단 거리로 가는 방법은 그냥 방문처리 하면서 가면 됨(최단 거리가 아닐 경우 해당 점을 더 나중에 방문하게 되므로 고려할 필요x)
2. 최단 거리로 가되 출발점과 도착점이 정해져 있지 않으므로 모든 점을 돌면서 최단 거리를 리스트에 저장
3. 2번의 리스트에서 가장 큰 값이 바로 가장 멀리 떨어진 보물 사이 거리(걸리는 시간)
"""
from copy import deepcopy
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
    global row, col
    visited = deepcopy(mapp)
    length = 0
    temp = 0
    visited[i][j] = 'W'
    q = [(i,j,0)]
    while len(q):
        y,x,l = q.pop(0)
        length = l
        for dx, dy in move:
            xx = x+ dx
            yy = y+ dy
            if 0<=xx<col and 0<=yy<row and visited[yy][xx] == 'L':
                visited[yy][xx] = 'W'
                q.append((yy,xx,l+1))
    res.append(length)


row, col = map(int, input().split())
mapp = []
for _ in range(row):
    mapp.append(list(input()))

res = []
for i in range(row):
    for j in range(col):
        if mapp[i][j] == 'L':
            bfs(i,j)
print(max(res))

"""
위 풀이가 원래 내 풀이고, 이 풀이가 python3으로 돌리면 시간초과가 나서 다른 사람 코드 참고해서 짠 코드가 아래 코드
아래 코드는 100% 이해 못 한 상태(res 값)
두 개 코드 전부 pypy로 돌리면 시간 초과 안 남(아래코드가 200ms 더 빠름)
"""

from collections import deque
import sys
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
    global row, col, result
    res = []
    visited = [[0]*col for _ in range(row)]
    q = deque()
    q.append((i,j,0))
    visited[i][j] = 1
    while len(q):
        y,x,l = q.popleft()
        for dx, dy in move:
            xx = x+ dx
            yy = y+ dy
            if 0<=xx<col and 0<=yy<row and mapp[yy][xx] == 'L' and not visited[yy][xx]:
                visited[yy][xx] = 1
                q.append((yy,xx,l+1))
                res.append(l+1)
    if len(res) and result < max(res):
        result = max(res)


row, col = map(int, sys.stdin.readline().split())
mapp = []
for _ in range(row):
    mapp.append(list(sys.stdin.readline()))

result = 0
for i in range(row):
    for j in range(col):
        if mapp[i][j] == 'L':
            bfs(i,j)
print(result)