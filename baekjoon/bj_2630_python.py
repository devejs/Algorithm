"""
2630. 색종이 만들기
210409 Solution
1. 시작 좌표, 사이즈를 큐에 담아서 큐가 빌 때까지 반복
2. 시작 좌표값(0 or 1) 과 동일한지 체크해서 동일하면 해당 값 리턴, 동일하지 않으면 4분할 큐에 추가
3. 리턴된 값은 0일때 1일때 따로 더하기(배열 인덱스)
"""
def check(i,j, n):
    clr = paper[i][j]
    for ii in range(i, i+n):
        for jj in range(j, j+n):
            if paper[ii][jj] != clr:
                return -1
    return clr

num = int(input())
paper = []
q = [(0,0,num)]
ans = [0,0]

for _ in range(num):
    paper.append(list(map(int, input().split())))

while(len(q)):
    i,j,n = q.pop(0)
    res = check(i,j,n)
    if res == -1:
        size = n//2
        q.append((i,j,size))
        q.append((i, j+size, size))
        q.append((i+size, j, size))
        q.append((i+size, j+size, size))
    else:
        ans[res] += 1

print(ans[0])
print(ans[1])

"""
분할 정복으로 풀면 훨씬 빠른듯. 다시 풀어보기..
"""