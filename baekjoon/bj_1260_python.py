"""
1260. DFS와 BFS
1. 그래프 양방향이므로 각각 설정해줌
2. DFS는 재귀
3. BFS는 큐
"""
def dfs(v):
    dfs_search.append(v)
    for i in graph[v]:
        if not i in dfs_search:
            dfs(i)

def bfs(vertex):
    q = [vertex]
    while len(q):
        v = q.pop(0)
        bfs_search.append(v)
        for i in graph[v]:
            if not (i in bfs_search or i in q):
                q.append(i)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs_search = []
bfs_search = []
dfs(v)
bfs(v)
for i in dfs_search:
    print(i, end=' ')
print()
for i in bfs_search:
    print(i, end=' ')

