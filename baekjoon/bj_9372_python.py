"""
9372. 상근이의 여행
210324 Solution
그래프
0. 스패닝 트리 -> 간선의 개수 = 노드 개수-1
1. 그러나 0번이 의심이 갔던 나는 그냥 연결 그래프 풀던 대로 풀이함
2. BFS로 가까운 너비부터 탐색, 방문한 노드는 큐에 넣지 않음
3. 노드 방문시 새 비행기 루트(간선)을 지나기 때문에 cnt++
"""
import sys
tc = int(input())
input = sys.stdin.readline
for tc in range(1, 1+tc):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    start = 0
    res = 0
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        if i == 0:
            start = a
    # res = n-1
    visited = [0]*(n+1)
    q= [start]
    visited[start] = 1
    while len(q):
        node = q.pop(0)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                res += 1
                q.append(i)
    print(res)

"""
표준 입출력으로 풀 경우 시간초과 발생
"""
