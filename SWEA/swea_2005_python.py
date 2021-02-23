"""
2005. 파스칼의 삼각형
210223 Solution
1. 규칙 구해서 반복문
규칙: 아래 행 index 값 = 위 행 index 값 + 위 행 index-1 값
"""

tc = int(input())
for tc in range(1,tc+1):
    size = int(input())
    triangle = []
    for i in range(1, size+1):
        if i==1:
            triangle.append([1])
        else:
            arr = []
            for j in range(i):
                if j == 0 or j == i-1:
                    arr.append(1)
                else:
                    arr.append(triangle[i-2][j-1]+triangle[i-2][j])
            triangle.append(arr)

    print(f"#{tc}")
    for i in triangle:
        for j in i:
            print(j, end=' ')
        print()
