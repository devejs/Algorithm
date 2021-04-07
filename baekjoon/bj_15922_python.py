"""
15922. 아우으 우아으이야!!
210406 Solution
1. 시작 좌표, 종료 좌표 나누기
2. 현재 위치 기록
3. 순서대로 선분의 합을 더하고 현재 위치 업데이트
4. 시작 좌표가 현재 위치보다 작다면 선분이 중복되는 것이므로 종료 좌표에 따라 선분의 합 더하기
"""
num = int(input())
start = []
end = []
sum = 0
for _ in range(num):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
loc = start[0]
for i in range(num):
    if start[i] >= loc:
        sum += end[i]-start[i]
    else:
        if end[i] >=loc:
            sum += end[i]-loc
        else:
            continue
    loc = end[i]

print(sum)

"""
정렬 문제라는데 정렬로는 어떻게 풀지 모르겠고 그냥 그리디로 풀었다
"""