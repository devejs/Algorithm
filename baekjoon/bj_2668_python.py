"""
2668. 숫자 고르기
210203 Solution
1. 사이클 찾기
"""
n = int(input())
data = []
result = []
route = []
for _ in range(n):
    data.append(int(input()))

def find_me(index):
    if index < len(data):
        if index in route:
            if index == route[0]:
                result.extend(route)
        else:
            route.append(index)
            find_me(data[index] - 1)
for i in range(n):
    find_me(i)
    route = []

result = list(set(result))
result.sort()
print(len(result))
for i in result:
    print(i+1)


"""
처음에 dfs로 풀다가 끝나는 지점을 잘 못 찾아서 구글링함
"""
