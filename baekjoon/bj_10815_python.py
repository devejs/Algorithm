"""
10815. 숫자 카드
1. 이분 탐색은 재귀로 구현 
2. 항상 중간 값을 구해서 좌우로 나눠주기 때문에 처음값, 끝 값이 필요하다
"""
def find(start, end, value):
    if start > end:
        return 0
    mid = (start+end) // 2
    if having[mid] == value:
        return 1
    elif having[mid] > value:
        # 왼쪽으로
        return find(start, mid-1, value)
    else:
        # 오른쪽으로
        return find(mid+1, end, value)


n = int(input())
having = list(map(int,input().split()))
having.sort()
m = int(input())
cards = list(map(int,input().split()))
result = []

for c in cards:
    result.append(find(0, n-1, c))

for i in result:
    print(i, end=' ')


"""
이분탐색 for문으로도 구현
"""