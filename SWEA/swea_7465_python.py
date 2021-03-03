"""
7465. 창용 마을의 개수
210303 Solution
1. 백준 회장 찾기 문제, dfs
2. 양방향 그래프 만들어 방문처리하여 dfs로 탐색하기
"""

def dfs(v):
    in_group[v] = 1
    for i in graph[v]:
        if not in_group[i]:
            dfs(i)


tc = int(input())
for tc in range(1,tc+1):
    num, rel = map(int, input().split())
    graph = [[] for _ in range(num+1)]
    for _ in range(rel):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    in_group = [0 for _ in range(num+1)]
    count = 0

    for i in range(1, num+1):
        if not in_group[i]:
            dfs(i)
            count += 1
    print(f"#{tc} {count}")
