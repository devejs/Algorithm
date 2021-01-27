"""
1206. View
210125 Solution
1. 리스트 for문 돌려 좌우 2칸의 최대 높이를 구함
2. 내 높이가 1보다 크면 조망권은 내 높이 - 최대 높이
"""

for i in range(10):
    length = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    for index in range(2, length-2):
        compare_list = buildings[index-2: index] + buildings[index+1: index+3]
        if buildings[index] > max(compare_list):
            count += buildings[index] - max(compare_list)
    print(f"#{i+1} {count}")
