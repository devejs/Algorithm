"""
1949. 등산로 조성
210305 Solution
최대 깊이를 구하는 dfs 문제
1. 배열에서 최댓값을 구한다.
2. 배열을 돌면서 최댓값인 부분에서만 dfs 탐색을 시작한다.
3. 상하좌우를 탐색해 내 값보다 작은 값은 dfs 탐색하고, 내 값보다 클 경우에는 깎을 수 있는지 봐서 깎아서 dfs 탐색
"""
move = [(-1,0),(1,0),(0,-1),(0,1)] # y,x, 상하좌우
 
def dfs(depth,chance,y,x):
    global size,k
    if res[0] < depth:
        res[0] = depth
    for yy, xx in move:
        if 0<= y+yy < size and 0<= x+xx < size and not visited[y+yy][x+xx]:
            if mapp[y][x] > mapp[y+yy][x+xx]:
                visited[y+yy][x+xx] = 1
                dfs(depth+1, chance, y+yy, x+xx)
                visited[y+yy][x+xx] = 0
            else:
                if chance == 1:
                    for cnt in range(1,k+1):
                        if mapp[y][x] > mapp[y+yy][x+xx]-cnt:
                            visited[y+yy][x+xx] = 1
                            mapp[y+yy][x+xx] -= cnt
                            dfs(depth + 1, chance-1, y + yy, x + xx)
                            mapp[y + yy][x + xx] += cnt
                            visited[y + yy][x + xx] = 0
 
 
tc = int(input())
for tc in range(1,tc+1):
    size, k = map(int, input().split())
    mapp = []
    maxx = 0
    for i in range(size):
        mapp.append(list(map(int, input().split())))
        temp = max(mapp[i])
        if temp > maxx:
            maxx = temp
    visited = [[0]*size for _ in range(size)]
    res = [1]
    for i in range(size):
        for j in range(size):
            if mapp[i][j] == maxx:
                visited[i][j] = 1
                dfs(1,1,i,j)
                visited[i][j] = 0
 
    print(f"#{tc} {res[0]}")

"""
처음에 BFS로 풀었다가 이렇게 최대 깊이를 구해야하는 문제는 BFS가 아니라는 걸 깨닫고 DFS로 풀었더니 바로 풀렸다.
K를 깎는게 까다로웠는데 어차피 가장 최소로 깎는 것이 제일 유리하기 때문에 카운트로 돌면서 최소한으로 깎았고(break 추가가 안돼있네),
나보다 큰 친구를 만났고 깎을 수 있다면 깎아서 도는 걸로 작성했다.
"""