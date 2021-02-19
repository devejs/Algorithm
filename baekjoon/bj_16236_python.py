"""
16236. 아기 상어
210219 Solution
1. BFS, 상어 위치에서 상하좌우 탐색
2. 상어의 크기가 크거나 같으면 큐에 넣고, 먹을 수 있으면 fish 스택에 추가로 넣는다.(최우선 경우의 수 찾기 위함; 위->왼)
3. 상하좌우 탐색이 끝나면 동일한 거리 안에 먹을 수 있는게 있는지 보고 있으면 상어 이동(재할당 및 큐, 스택 초기화, 크기나 식사 횟수 증가)
4. 3을 통해 지난 길은 0으로 바꿔 상어가 통과할 수 있게 함
5. 기본적으로 0은 지나갈 수 있어야 하나, 물고기를 찾지 못하고 계속 탐색할 경우 이미 지나온 길은 방문할 필요 없으므로 visited 사용
6. 최소한 같은 거리 안에 있는 위치는 다 탐색해야 하므로 거리가 같은 위치가 큐에 남아 있으면 계속 탐색
"""

length = int(input())
maps= []
for _ in range(length):
    maps.append(list(map(int,input().split())))

# 식사 횟수, 크기, x좌표(열), y좌표(행)
shark = [0, 2]
# find baby shark
for index, row in enumerate(maps):
    if 9 in row:
        x = row.index(9)
        maps[index][x] = 0
        shark.extend([x, index])
        break

time = 0
visited = [[0]*length for _ in range(length)]
# 상 좌 우 하
moves = [(0,-1),(-1,0),(1,0),(0,1)]
# 전달 정보: x좌표, y좌표, 거리
q = [(shark[2], shark[3], 0)]
fishes = []
while len(q):
    x, y, d = q.pop(0)
    for move in moves:
        if 0<= x+move[0] < length and 0<= y+move[1] < length and not visited[y+move[1]][x+move[0]]:
            visited[y + move[1]][x + move[0]] = 1
            if 0 < maps[y+move[1]][x+move[0]] < shark[1]:
                fishes.append((x+move[0], y+move[1]))
                q.append((x+move[0], y+move[1], d+1))
            elif maps[y+move[1]][x+move[0]] == shark[1] or maps[y+move[1]][x+move[0]] == 0:
                q.append((x + move[0], y + move[1], d + 1))
    if len(fishes) and len(q) and q[0][2] != d:
        time += d+1
        fishes.sort(key=lambda fish : (fish[1], fish[0]))
        xx, yy = fishes.pop(0)
        maps[yy][xx] = 0
        shark[2] = xx
        shark[3] = yy
        q = [(xx, yy, 0)]
        shark[0] += 1
        if shark[0] == shark[1]:
            shark[1] += 1
            shark[0] = 0
        visited = [[0]*length for _ in range(length)]
        fishes = []

print(time)

"""
최단거리 구하는 문제는 dfs가 아니라 bfs로 푸는 게 유리함
깊이 때문에 dfs를 써야 되나 했는데 그냥 bfs로 풀되 깊이는 넘겨주면 됨
- 거리 기준이 0인지 1인지 기준에 대해 헷갈리지 말 것!
- 마지막에 TC 통과 못했던 원인: 처음에 fish를 큐 돌때마다 할당했더니 거리 레벨이 2 이상일 때 물고기를 찾으면 바로 이동해버리는 문제
-> 6번으로 해결
"""
