"""
1018. 체스판 다시 칠하기
210409 Solution
1. 파리잡기처럼 가능한 네모 완전탐색
2. 판이 W로 시작하는 경우, B로 시작하는 경우가 있으므로 두 가지 경우 전부 탐색
3. 8x8 잘라낸 판에서 W와 B가 번갈아가는지 체크(2 나머지 및 인덱스 활용)
4. 칠하는 답이 최소인 경우 출력
"""
def check_board(i,j, clr):
    cnt = 0
    for y in range(i, 8 + i):
        clr+=1
        for x in range(j, 8 + j):
            if board[y][x] != color[clr%2]:
                cnt += 1
            clr+=1
    return cnt

n, m = map(int, input().split())
board = []
color = ['B', 'W']
for _ in range(n):
    board.append(input())

ans = 64
for i in range(n-7):
    for j in range(m-7):
        cnt1 = check_board(i,j,0)
        cnt2 = check_board(i,j,1)
        res = cnt1 if cnt1 <= cnt2 else cnt2
        if ans > res:
            ans = res
print(ans)