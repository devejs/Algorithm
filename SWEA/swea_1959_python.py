"""
1959. 두 개의 숫자열
210225 Solution
1. 움직일 배열(크기가 작은 배열)을 구한다
2. 이동할 수 있는 범위를 구한다
3. 배열을 움직이면서(인덱스++) 작은 배열의 크기만큼 각 인덱스를 곱한다
"""

def move(a, b, i):
    result = 0
    for k in range(len(a)):
        result += a[k]*b[k+i]
    return result

tc= int(input())
for tc in range(1, tc+1):
    a, b = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    compared= b>a
    moving = b-a if compared else a-b
    result = 0
    if compared:
        for i in range(moving+1):
            temp = move(list_a, list_b, i)
            if result < temp:
                result = temp
    else:
        for i in range(moving+1):
            temp = move(list_b, list_a, i)
            if result < temp:
                result = temp

    print(f"#{tc} {result}")



