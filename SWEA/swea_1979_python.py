"""
1979. 어디에 단어가 들어갈 수 있을까
210224 Solution
1. 방문 큐 열, 행 두개
2. 이중 배열 돌면서 값이 1이고 방문하지 않은 인덱스에 대해 bfs
3. bfs는 열인지 행인지 체크하여 각각 재귀로 돌면서 길이가 맞으면 카운트++, 부족하거나 초과하면 continue
"""
def bfs(i,j, depth, dir):
    depth += 1
    if dir:
        visited_col[i][j] = 1
        if j == size-1 and depth == length:
            ans[0] += 1
        elif j < size-1 and puzzle[i][j+1] == '1':
            bfs(i,j+1, depth, True)
        else:
            if depth == length:
                ans[0] += 1
    else:
        visited_row[i][j] = 1
        if i == size-1 and depth == length:
            ans[0] += 1
        elif i < size-1 and puzzle[i+1][j] == '1':
            bfs(i+1, j, depth, False)
        else:
            if depth == length:
                ans[0] += 1

tc= int(input())
for tc in range(1, tc+1):
    size, length = map(int,input().split())
    puzzle = []
    for i in range(size):
        puzzle.append(input().split())
    ans = [0]
    visited_col = [[0]*size for _ in range(size)]
    visited_row = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if puzzle[i][j]=='1':
                if j <= size-length and not visited_col[i][j]:
                    bfs(i,j,0,True)
                if i <= size-length and not visited_row[i][j]:
                    bfs(i,j,0,False)
    print(f"#{tc} {ans[0]}")

"""
그냥 방문 처리 없는 BFS 완전탐색으로 풀려고 했는데 그렇게 푸니까 1이 K 개수보다 큰 경우,
두번째 세번째 1에서 중복 카운트가 올라가는 문제(왼쪽 카운트를 안해서 생긴 문제)
그래서 결국 방문 체크 배열을 두개나 만들어줬는데 이걸 어떻게 리팩토링할지 생각해보기
두개 만들어준 이유는 열 따로 행 따로라.. 열에서 체크했다고 행에서 체크 안할 수는 없으니

그리고 처음에는 아예 bfs 안에서 열, 행을 같이 처리해주고 싶었는데 그러면 깊이 전달하는 부분에서 너무 꼬여버려서 나눔
"""

