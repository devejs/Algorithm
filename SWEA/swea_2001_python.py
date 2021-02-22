"""
2001. 파리 퇴치
210222 Solution
1. 누가 봐도 완전탐색 거꾸로 봐도 완전탐색
2. N크기 정사각형 안에서 M크기 정사각형이 움직일 수 있는 거리를 구하고, 행측과 열측으로 움직인 결과를 각각 구한다.
3. 이중 포문으로 열과 행이 달라졌을 경우를 세되, 반복문 안에서 m크기만큼 돌면서 정사각형의 값을 전부 더한다.
4. result값과 비교하여 큰 값을 걸러냄
"""

tc = int(input())
for tc in range(1,tc+1):
    n, m = map(int, input().split())
    mosq = []
    for _ in range(n):
        mosq.append(list(map(int,input().split())))
    move = n-m+1
    result = 0
    for row in range(move):
        for col in range(move):
            sum = 0
            for i in range(m):
                for j in range(m):
                    sum += mosq[row+i][col+j]
            if sum > result:
                result = sum
    print(f"#{tc} {result}")
