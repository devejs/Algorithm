"""
1258. 행렬찾기
파리잡기 문제처럼 풂
1. 직사각형임이 보장되어 있으므로 0이 아닌 값을 찾았을 때 가로 길이 먼저 구하기
2. 세로 길이 구하면서 각 열마다 가로길이만큼을 방문 처리 해 줌
3. 정렬은 크기 > 행 순
1260 문제의 선행문제
"""
tc = int(input())
for tc in range(1,tc+1):
    size = int(input())
    bottles = []
    for _ in range(size):
        bottles.append(list(map(int, input().split())))
    ans = []

    for i in range(size):
        for j in range(size):
            x = 0
            y = 0
            if bottles[i][j]:
                while j+x < size and bottles[i][j+x]:
                    x += 1
                while i+y < size and bottles[i+y][j]:
                    for k in range(x):
                        bottles[i+y][j+k] = 0
                    y += 1
                ans.append((x,y))

    ans.sort(key=lambda x : ((x[0]*x[1]), x[1]))
    print(f"#{tc} {len(ans)}", end=' ')
    for x, y in ans:
        print(f"{y} {x}", end=' ')
    print()
