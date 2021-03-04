"""
4012. 요리사
210304 Solution
1. 조합을 두 번 구해야 하는 문제. 
2. 첫번째 조합(사용할 식재료)는 dfs로 구하고, 두번째 조합은 for문과 combination 라이브러리 두 개로 구현
3. dfs를 통해 n//2개만큼 방문한 배열은 곧 두 개의 배열로 분리할 수 있다.
    방문처리 된 배열(n//2개 원소), 방문처리 안 된 배열(n//2개 원소)
4. 두 개의 배열은 또 각각 2개 원소씩을 골라야 하는데, 이 때 combinations 라이브러리 사용
5. 4번에서 반환된 배열을 각각 돌면서 두 개의 식재료 맛을 더해준다(ij와 ji가 다르기 때문)
6. 4번 값이 작으면 재할당해주면서 완전탐색
7. 시간 초과의 핵심은 dfs할 때 for문의 범위!!
`for i in range(k, n)`
-> 조합이고 이미 낮은 깊이에서 k인덱스 전의 값들을 골랐기 때문에 더이상 탐색할 필요가 없다
-> 여기서 k가 아니라 0부터 탐색할 경우 순열이 된다
"""
from itertools import combinations

def calc(visited):
    a = []
    b = []
    for i,v in enumerate(visited):
        if v:
            a.append(i)
        else:
            b.append(i)
    res1 = res2 = 0
    a = list(combinations(a, 2))
    b = list(combinations(b, 2))
    for i,j in a:
        res1 += (recipes[i][j]+recipes[j][i])
    for i,j in b:
        res2 += (recipes[i][j]+recipes[j][i])
    res = abs(res1-res2)
    return res

def dfs(k, depth):
    global n
    if depth == n//2:
        res = calc(check)
        if res < ans[0]:
            ans[0] = res
        return
    for i in range(k,n):
        if not check[i]:
            check[i] = 1
            dfs(i+1, depth+1)
            check[i] = 0

tc = int(input())
for tc in range(1,tc+1):
    n = int(input())
    recipes = []
    for _ in range(n):
        recipes.append(list(map(int, input().split())))
    check = [0]*n
    ans = [999999]
    dfs(0, 0)
    print(f"#{tc} {ans[0]}")

"""
시간 초과로 고생을 많이 했다.
combination 라이브러리를 안 쓰고 구현하고 싶었는데 for문 써서 조합 구현하는 것보다 라이브러리가 더 빨랐다. 
두 번째 조합 구할 때 제일 큰 인풋에서 한 5~6초 정도 차이

처음에는 아예 조합 구하는걸 구현해서 두번 다 적용하고 싶었는데 그건 실패함(깊이때문에)
-> 이 것도 나중에 실력 쌓이면 더 도전해보기

위 풀이 3번에서 처음에는 일일이 다 배열을 넘겨주고 나중에 차집합으로 구했는데 이것도 시간이 더 소요된다.
시간뿐 아니라 메모리도 소요되는 작업이므로 방문배열을 통해 간단하게 처리해줄 수 있었다.

ex) [1,2,3,4]에서 어차피 식재료를 두개로 나눠서 각각 사용하기 때문에
[1,2]를 구하는 경우의 수나 [3,4]를 구하는 경우의 수가 동일한 결과를 낳는다.
이 부분을 구현하면 시간이 훨씬 줄 것 같은데 아직 이 부분에 대한 구현은 못 함.
!!!문제 탐구가 더 필요할 것 같다.
"""


# Combinations 안 쓴 버전(살짝 시간 초과함)

# def calc(comb):
#     global n
#     res1 = 0
#     res2 = 0
#     comp = list(set(range(n)) - set(comb))
#     for i in range(n//2-1):
#         for j in range(i+1,n//2):
#             res1 += recipes[comb[i]][comb[j]] + recipes[comb[j]][comb[i]]
#             res2 += recipes[comp[i]][comp[j]] + recipes[comp[j]][comp[i]]
#     return abs(res1-res2)