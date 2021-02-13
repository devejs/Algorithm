"""
2805. 농작물 수확하기
210213 Solution
1. 완전탐색할 경우 이차원 배열의 행에 따라 선택되는 열의 개수가 달라지는 것에 착안
2. 항상 홀수 크기이므로 중앙이 정해져 있고, 중앙 기준으로 양옆 ++
3. 선택되는 열이 줄어드는 순간은 행의 인덱스 > 중앙
4. 리스트 돌면서 규칙에 따른 열만 합에 추가
"""

tc_num = int(input())
for tc in range(1, tc_num+1):
    values = []
    sum = 0
    size = int(input())
    center = size // 2
    for i in range(size):
        values.append(list(map(int, list(input()))))
    for i, side in enumerate(values):
        sum += side[center]
        if i <= center:
            for n in range(1, i+1):
                sum += side[center-n]
                sum += side[center+n]
        else:
            for n in range(1, size-i):
                sum += side[center-n]
                sum += side[center+n]
    print(f"#{tc} {sum}")
