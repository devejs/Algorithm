"""
2660. 회장 뽑기
210215 Solution
1. 양방향 그래프 배열 생성
2. 각 노드(회원)마다 점수를 찾기 위해 for문
3. BFS, 큐에 연결된 노드를 넣되 방문 처리
4. 각 노드(회원)은 가장 큰 점수를 기록하고, 전체적으로는 가장 낮은 점수를 찾는다.
"""

num = int(input())
graph = [[] for _ in range(num)]
scores = [50]

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    else:
        # 양방향 그래프
        graph[a-1].append(b)
        graph[b-1].append(a)

for index in range(1, num+1):
    q= [(index, 0)]
    visited= [index]
    score = 0
    while len(q):
        v, depth = q.pop(0)
        flag = True
        for child in graph[v-1]:
            if not child in visited:
                visited.append(child)
                q.append((child, depth+1))
                flag = False
        if flag and depth > score:
            score = depth
    if score < scores[0]:
        scores = [score, index]
    elif score == scores[0]:
        scores.append(index)

print(f"{scores.pop(0)} {len(scores)}")
scores.sort()
for i in scores:
    print(f"{i}", end=" ")
