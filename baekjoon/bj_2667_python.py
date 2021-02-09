"""
2667. 단지번호 붙이기
210202 Solution
1. 주변에 집이 있는지 없는지 확인하기 위해 BFS
2. 모든 배열을 탐색하되 방문하거나 0인 곳은 방문할 필요가 없으므로 제외
3. 방문시 방문 체크 및 큐에 넣기, count++
4. 큐의 front 값을 출력해 상하좌우 검사하되 해당 값이 1이면 큐에 넣음
5. 큐에 더이상 방문할 곳이 없으면 단지가 끝남 -> 단지에 속한 집의 값 출력
"""
n = int(input())
move_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
h_map = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
count_list = []
q = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and h_map[i][j]:
            visited[i][j] = 1
            q.append((i,j))
            count = 0
            while (len(q)):
                a,b = q.pop(0)
                count += 1
                for x, y in move_list:
                    if 0<= a+y < n and 0<= b+x < n:
                        if not visited[a+y][b+x] and h_map[a+y][b+x]:
                            visited[a+y][b+x] = 1
                            q.append((a+y, b+x))
            count_list.append(count)
print(len(count_list))
count_list.sort()
for count in count_list:
    print(count)
