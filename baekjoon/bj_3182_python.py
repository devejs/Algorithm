"""
3182. 한둥이는 공부가 하기 싫어
210331 Solution
1. 처음 물어본 선배의 번호와 깊이를 저장, 물어볼 선배의 번호 변수 저장
2. dfs, 물어본 선배는 방문처리하고, 방문하지 않은 선배는 깊이 증가시켜 다음 선배로 넘어감
3. 이미 방문한 선배한테 도달했을 경우에 반복문 break, 이 때 깊이가 결과보다 클 경우에만 1번 값 변경
4. 어떤 선배한테서 시작했을 때 결과가 제일 클 지 구해야 하므로 1번부터 n번까지 반복
"""
n = int(input())
info = [0]
result = (0,0)
for _ in range(n):
    info.append(int(input()))
for i in range(1,n+1):
    visited = [0 for _ in range(n + 1)]
    if result[1] == n:
        break
    ask = i
    depth = 0
    while(1):
        if visited[ask]:
            if depth > result[1]:
                result = (i, depth)
            break
        else:
            depth += 1
            visited[ask] = 1
            ask = info[ask]
print(result[0])