"""
15562. 톱니바퀴(2)
210218 Solution
1. BFS
"""

gear_num = int(input())
gears = []
for _ in range(gear_num):
    gears.append(list(input()))
rotate_num = int(input())
rotations = []

for _ in range(rotate_num):
    rotations.append(map(int, input().split()))

for num, dir in rotations:
    q = [(num, dir)]
    visited = [1]*gear_num
    visited[num-1] = 0
    while len(q):
        n, d = q.pop(0)
        # 오른쪽 톱니 비교
        if n < gear_num:
            if visited[n] and gears[n-1][2] != gears[n][6]:
                q.append((n+1, d*(-1)))
                visited[n] = 0
        # 왼쪽 톱니 비교
        if n > 1:
            if visited[n-2] and gears[n-1][6] != gears[n-2][2]:
                q.append((n-1, d*(-1)))
                visited[n-2] = 0
        # 방향에 따른 회전
        if d == 1:
            last = gears[n-1].pop()
            gears[n-1].insert(0, last)
        elif d == -1:
            first = gears[n-1].pop(0)
            gears[n-1].append(first)
count = 0
for gear in gears:
    if gear[0] == '1':
        count += 1
print(count)
