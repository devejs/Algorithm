"""
9375. 패션왕 신해빈
210407 Solution
1. 해시; 딕셔너리 사용
2. 경우의 수 구하기
"""
tc = int(input())
for _ in range(tc):
    num = int(input())
    clothes = {}
    res = 1
    for _ in range(num):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    for key, value in clothes.items():
        res *= (value+1)
    print(res-1)