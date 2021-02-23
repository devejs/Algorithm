"""
1248. 공통 조상
210223 Solution
분할 정복으로 풀어야되는데 모르겠어서 그냥 평소 트리 풀듯이 풀었다.
1. 부모 노드를 가지고 있는 리스트, 자식 노드를 가지고 있는 리스트 두 개를 사용했다.
2. 각 노드의 모든 부모를 다 구하고, 이 때 depth를 저장해 놓는다.
3. 2에서 구한 두 부모 리스트에서 공통인 것중 깊이가 최소인 것이 바로 가장 가까운 공통 조상
4. 공통 조상은 자식 리스트에서 재귀로 자식의 개수를 리턴해서 구해준다.
"""

def find_parent(child, pars):
    if parent[child] == -1:
        return pars
    else:
        depth = len(pars)+1
        pars.append([parent[child], depth])
        return find_parent(parent[child], pars)

def close_common(v1, v2):
    commons = []
    compare = []
    for i in v2:
        compare.append(i[0])
    for i in v1:
        if i[0] in compare:
            commons.append(i)
    commons.sort(key=lambda x:x[1])
    if len(commons):
        return commons[0][0]
    else:
        return -1

def find_children(v):
    count = 1
    if len(child[v]):
        for i in child[v]:
            count += find_children(i)
        return count
    else:
        return count


tc = int(input())
for tc in range(1,tc+1):
    vertex, edge, v1, v2 = map(int, input().split())
    edges = list(map(int, input().split()))
    child = [[] for i in range(vertex+1)]
    parent = [-1]*(vertex+1)
    for i, v in enumerate(edges):
        if i % 2==0:
            # 부모 노드
            child[v].append(edges[i+1])
            # 자식 노드
            parent[edges[i+1]] = v

    v1_p = find_parent(v1, [])
    v2_p = find_parent(v2, [])
    print(v1_p)
    print(v2_p)

    ans_node = close_common(v1_p, v2_p)

    print(f"#{tc} {ans_node} {find_children(ans_node)}")




