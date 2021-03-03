"""
1952. 수영장
210303 Solution
1. 1년권을 제외하고 각 월마다 1일권을 살 경우, 1개월권을 살 경우, 3개월권을 살 경우로 나누면 그래프 완전탐색
2. 깊이를 월 수로 하여 권종마다 가격을 더해주는 방식으로 dfs
3. 마지막에 1년권과 가격을 비교하여 최종 가격 도출
"""
def dfs(depth, result):
    if result > ans[0]:
        return
    if depth >= 12:
        if result < ans[0]:
            ans[0] = result
        return
    if not plans[depth]:
        dfs(depth+1, result)
    else:
        for i in range(3):
            if i==0:
                new_result = result+prices[i]*plans[depth]
                dfs(depth+1, new_result)
            elif i==1:
                new_result = result + prices[i]
                dfs(depth+1, new_result)
            else:
                new_result = result + prices[i]
                dfs(depth+3, new_result)


tc = int(input())
for tc in range(1, tc+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    ans = [999999]

    dfs(0, 0)

    if ans[0] > prices[-1]:
        ans[0] = prices[-1]
    print(f"#{tc} {ans[0]}")