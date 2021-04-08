"""
1012. 유기농 배추
1. 덩어리 1 값을 찾는 문제이므로 bfs
2. 지날 때마다 방문처리 대신 0으로 바꿔줌으로써 중복이 안되게 함
3. 주변 큐가 끝날 때마다 카운트++
"""
def bfs(i,j):
    q = [(i,j)]
    while len(q):
        y, x = q.pop(0)
        for xx, yy in move:
            if 0 <= y+yy < size[1] and 0 <= x+xx < size[0] and mapp[y+yy][x+xx]:
                q.append((y+yy, x+xx))
                mapp[y+yy][x+xx] = 0

move = [(0,-1),(0,1),(1,0),(-1,0)]
tc = int(input())
for tc in range(1,tc+1):
    m, n, k = map(int, input().split())
    mapp = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        mapp[b][a] = 1
    count = 0
    size = [m,n]
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mapp[i][j]:
                mapp[i][j] = 0
                bfs(i,j)
                count += 1
    print(count)


"""
210408 다시 풀기
메모리 동일, 속도는 조금 느려진듯?
"""
def bfs(i,j):
    global m, n
    q = [(i,j)]
    num = 1
    mapp[i][j] = 0
    while len(q):
        y, x = q.pop(0)
        for yy, xx in move:
            if 0<= x+xx < m and 0<= y+yy < n and mapp[y+yy][x+xx]:
                mapp[y + yy][x + xx] = 0
                q.append((y+yy, x+xx))
                num += 1
    return num

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    mapp = [[0]*m for _ in range(n)]
    sum = 0
    res = 0
    for _ in range(k):
        x, y = map(int,input().split())
        mapp[y][x] = 1

    flag = False
    for i in range(n):
        for j in range(m):
            if mapp[i][j]:
                sum += bfs(i,j)
                res += 1
                if sum == k:
                    flag = True
                    break
        if flag:
            break
    print(res)