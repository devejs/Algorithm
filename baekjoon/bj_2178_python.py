"""
2178. 미로 탐색
210307 Solution
1. bfs로 상하좌우 탐색하되, 깊이를 같이 전달
2. (N,M)에 도착했을 때 깊이가 더 작으면 최소 깊이 갱신
"""
move = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
def bfs(i,j):
    depth = 1
    q = [(depth,i,j)]
    while len(q):
        d, y, x = q.pop(0)
        if d >= ans[0]:
            continue
        if y == n-1 and x == m-1 and d < ans[0]:
            ans[0] = d
            continue
        for yy, xx in move:
            if 0<= y+yy < n and 0<= x+xx < m and mapp[y+yy][x+xx] == '1' and not visited[y+yy][x+xx]:
                visited[y + yy][x + xx] = 1
                q.append((d+1, y+yy, x+xx))

n, m = map(int, input().split())
mapp = []
maxx = 0
for i in range(n):
    mapp.append(input())
    maxx += mapp[i].count('1')
visited = [[0]*m for _ in range(n)]
ans = [maxx]
visited[0][0] = 1
bfs(0,0)
print(ans[0])

"""
최대 깊이 탐색은 dfs, 최소 길이 탐색은 bfs. 자주 헷갈리니 정리해두고 기억할 것
신기한건 이미 d>=ans[0]에서 걸렀다고 생각해서 그 아래 d < ans[0]을 처리 안해줬더니 오히려 시간이 더 걸림
해줬을 때 96ms -> 안해줬을 때 100ms
"""