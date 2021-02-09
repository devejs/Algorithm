"""
2669. 직사각형 네개의 합집합의 면적 구하기
210202 Solution
1. 좌표계를 그리기 위해 가장 큰 x,y 좌표를 구하여 좌표계(리스트)를 만듦
2. 사각형의 넓이에 해당하는 리스트의 값 체크(1)
3. 겹친 면적은 어차피 제외되므로 1인 값을 전부 더하면 합집합의 면적
"""
sqr_list = []
for _ in range(4):
    sqr_list.append(list(map(int, input().split())))
max_x = max(sqr[2] for sqr in sqr_list)
max_y = max(sqr[3] for sqr in sqr_list)
area = [[0]*max_x for _ in range(max_y)]

for sqr in sqr_list:
    for y in range(sqr[1],sqr[3]):
        for x in range(sqr[0], sqr[2]):
            area[y][x] = 1

area_sum = 0
for ar in area:
    area_sum += sum(ar)
print(area_sum)
