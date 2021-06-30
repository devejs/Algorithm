"""
14719. 빗물
210630 Solution
1. 블록 높이에 따라 2차원 맵에 1,0으로 표기
2. 행마다 3~ 반복
3. 행의 값에 한 번 1이 나오면 wall 플래그를 만들어 그 다음부터 나오는 0을 카운트
4. 1이 나올 때마다 그 동안 쌓인 카운트를 결과에 더하기; 카운트 초기화
5. 행의 마지막 열일 때만 주의: 1이면 더하고, 0이면 블록 사이가 아니므로 지금까지 더한 카운트를 버림
"""

def get_map(h,w,lst):
    temp = [[0]*w for _ in range(h)]
    for i,v in enumerate(lst):
        hei = h-v
        for row in range(h):
            if row >= hei:
                temp[row][i] = 1
    return temp

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
mapp = get_map(h,w,blocks)
res = 0

for row in range(h):
    wall = False
    cnt = 0
    for col in range(w):
        if col == w-1:
            if mapp[row][col] and wall:
                res += cnt
        else:
            if mapp[row][col]:
                if wall:
                    res += cnt
                    cnt = 0
                else:
                    wall = True
            else:
                if wall:
                    cnt += 1
print(res)

"""
처음에는 단순히 왼쪽 wall값을 넣어서 오른쪽에 나오는 값에 따라 리스트에 넣어서 최종 계산하는 방식으로 풀이
이 경우 반례가 너무 많이 생김
아예 2차원 맵으로 그려서 행으로 체크하니까 보임
"""