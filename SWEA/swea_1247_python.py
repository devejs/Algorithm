"""
1247. 최적 경로
210223 Solution
코드가 몹시 구리다. 리팩토링 및 재 풀이 필요.
1. dfs로 풀되 시작과 끝이 정해져있기 때문에 중간값만 큐(배열)에 넣었다.
2. 들를 곳의 순서를 정하는 순열 문제이므로 배열에서 한가지 값을 선택해 거리를 구하고, dfs를 재귀로 돌렸다.
3. 가지치기를 위해 d(거리)값이 이전에 구한 거리 값보다 크다면 바로 해당 dfs는 종료
"""
def get_distance(to, frm):
    x = to[0]-frm[0]
    y = to[1]-frm[1]
    return abs(x)+abs(y)

def dfs(cur, unvisited, d):
    if len(unvisited)==0:
        d += get_distance(cur, end)
        if d < dist[0]:
            dist[0]= d
        return
    for _ in range(number):
        temp = unvisited.pop(0)
        new_d = d+get_distance(cur, temp)
        if new_d > dist[0]:
            return
        dfs(temp, unvisited[:], new_d)
        unvisited.append(temp)
import sys
# sys.stdin=open("input.txt","r")
# tc = int(input())
for tc in range(1, tc+1):
    number = int(input())
    places = list(map(int, input().split()))
    dist = [999999]
    unvisited = []
    start = [places[0], places[1]]
    end = [places[2], places[3]]
    for i in range(4,len(places),2):
        unvisited.append([places[i], places[i+1]])

    dfs(start, unvisited, 0)

    print(f"#{tc} {dist[0]}")