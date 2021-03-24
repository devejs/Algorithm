"""
1449. 수리공 항승
210324 Solution
그리디
1. 앞에서부터 테이프 붙여나가기
2. 테이프 겹쳤으면 continue, 겹치지 않았으면 테이프 범위에 따라 새로 붙이기
3. 2번에서 새로 붙이되 최대한 테이프끼리 겹치지 않도록 붙이기
"""
n, l = map(int,input().split())
locs = list(map(int, input().split()))
locs.sort()
fixed = 0
cnt = 0
for i in locs:
    if i > fixed:
        fixed = i+l-0.5
        cnt += 1
    elif i == fixed:
        fixed = i+l
        cnt += 1

print(cnt)


