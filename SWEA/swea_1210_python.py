"""
1210. Ladder1
210126 Solution
1. 마지막 줄에서 시작; 출발 x좌표 저장
2. 이전 x좌표와 현재 좌표 비교
3. 현재 좌표의 left, right값 비교
4. left/right/up 이동하며 이전 x좌표 = 현재 좌표
"""

for _ in range(10):
    arr = []
    tc_num = int(input())
    dx = [-1, 1] # 좌우
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    cur_x = arr[-1].index(2)
    cur_y = 98
    past_x = cur_x

    while (cur_y > 0 ):
        if cur_x == 0:
            left = 0
            right = arr[cur_y][cur_x + dx[1]]
        elif cur_x == 99:
            left = arr[cur_y][cur_x + dx[0]]
            right = 0
        else:
            left = arr[cur_y][cur_x + dx[0]]
            right = arr[cur_y][cur_x + dx[1]]

        if past_x > cur_x:
            past_x = cur_x
            if left:
                cur_x += dx[0]
            else:
                cur_y -= 1
        elif past_x < cur_x:
            past_x = cur_x
            if right:
                cur_x += dx[1]
            else:
                cur_y -= 1
        else:
            past_x = cur_x
            if left:
                cur_x += dx[0]
            elif right:
                cur_x += dx[1]
            else:
                cur_y -= 1

    print(f"#{tc_num} {cur_x}")

"""
삽질 기록
1. x,y 좌표 헷갈림
2. 좌,우 이동시 left==right==1 되는 케이스 고려 안 함
3. 좌, 우 이동 후 up할때 past_x 재할당 안함.........
"""
