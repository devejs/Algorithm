"""
1953. 탈주범 검거
210304 Solution
1. bfs로 터널의 종류에 따라 너비 탐색
2. 이동할 위치에 터널이 있는지, 있으면 터널이 연결되는지 체크
3. 마지막에 있을 수 있는 위치는 연결된 방문한 터널이므로 탐색할 때마다 방문 가능하면 count++
4. 이 경우에는 큐에 담긴 터널들이 연결된 방문할 터널이므로 큐의 값을 count에 더함
5. 주의할 점! 처음에 탐색할 때 연결되지 않은 터널이더라도 나중에 연결될 수 있으므로 방문처리하면 안 됨
"""
# 상하좌우, (x,y) , dir 동일
move = [(0,-1),(0,1),(-1,0),(1,0)]
direction = {
    "0": [],
    "1": [0,1,2,3],
    "2": [0,1],
    "3": [2,3],
    "4": [0,3],
    "5": [1,3],
    "6": [1,2],
    "7": [0,2]
}

def reverse_dir(idx):
    if idx%2 ==0:
        return idx+1
    else:
        return idx-1

# 0 상 1 하 2 좌 3 우
def search(ori,mv,dir):
    global row, col
    x, y = ori
    xx, yy = mv
    if 0<=x+xx<col and 0<=y+yy<row and not visited[y+yy][x+xx]:
        if dir in direction[mapp[y+yy][x+xx]]:
            visited[y + yy][x + xx] = 1
            return [(x+xx, y+yy)]
    return []

def bfs(x,y):
    global time
    q = [(x,y)]
    t = 1
    count = 0
    while t != time:
        count += len(q)
        new_q = []
        while len(q):
            j,i = q.pop(0)
            for d in direction[mapp[i][j]]:
                new_q.extend(search((j,i),move[d],reverse_dir(d)))
        t += 1
        q = new_q
    return count+len(q)

tc = int(input())
for tc in range(1,tc+1):
    row, col, y, x, time = map(int, input().split())
    mapp = []
    for _ in range(row):
        mapp.append(input().split())
    visited = [[0]*col for _ in range(row)]
    visited[y][x] = 1
    ans = bfs(x,y)
    print(f"#{tc} {ans}")

