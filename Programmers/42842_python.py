"""
프로그래머스 > 완전탐색 > 카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
1. 모든 타일의 합은 가로*세로
2. 2*가로 + 2*(세로-2) = 갈색 타일
3. 가로*세로 곱한 값이고 가로나 세로는 1이 아니므로 세로 범위를 summ//2까지 두고 반복
4. 위 값을 만족하는 가로, 세로 값은 2개(가로, 세로 값이 다른 경우) 혹은 1개이므로 y를 증가시키면서 먼저 나온 y(세로가 작을 때) 리턴
"""
def solution(brown, yellow):
    summ = brown + yellow
    for y in range(1, summ//2+1):
        if summ % y == 0:
            x = summ//y
            if x+y-2 == brown/2:
                return [x,y]