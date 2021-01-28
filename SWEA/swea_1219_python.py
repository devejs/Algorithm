"""
1219. 길찾기
210128 Solution
1. Data 저장은 문제에 나와 있는 대로 배열 2개로 구성
2. 노드 방문시 방문 체크 후 이웃 노드 개수 카운트
3-1. 이웃 노드가 0개: 스택 확인해 방문하지 않은 노드 찾기
3-2. 이웃 노드가 1개: 다음 노드로 이동
3-3. 이웃 노드가 2개: 방문하지 않은 이웃 노드를 확인하고 스택에 추가 후 하나의 노드 방문
4. 도착지를 못찾으면 break; result는 false(0)
"""

for _ in range(10):
    tc_num, length = input().split()
    tc_list = list(map(int, input().split()))
    addr = [[-1 for _ in range(100)] for _ in range(2)]
    loc_num = 0
    for index in range(len(tc_list)):
        if index % 2 == 0:
            if addr[0][tc_list[index]] == -1:
                addr[0][tc_list[index]] = tc_list[index+1]
                loc_num += 1
            else:
                addr[1][tc_list[index]] = tc_list[index+1]
    visited = [0 for _ in range(100)]
    left_stack = []
    searching = 0
    result = 1
    while (searching != 99):
        visited[searching] = 1
        if addr[0][searching] == -1:
            if len(left_stack):
                searching = left_stack.pop()
            else:
                result = 0
                break
        elif addr[1][searching] == -1:
            if visited[addr[0][searching]]:
                if len(left_stack):
                    searching = left_stack.pop()
                else:
                    result = 0
                    break
            else:
                searching = addr[0][searching]
        else:
            if visited[addr[0][searching]] == 0 or visited[addr[1][searching]] == 0:
                if not searching in left_stack:
                    left_stack.append(searching)

                if visited[addr[0][searching]]:
                    searching = addr[1][searching]
                else:
                    searching = addr[0][searching]
            else:
                if len(left_stack):
                    searching = left_stack.pop()
                else:
                    result = 0
                    break
    print(f"#{tc_num} {result}")

"""
제출 후 잘못 낸 것 발견
while문 첫번째 elif에서 인덱스 1을 0으로 잘못 썼는데도 제대로 돌아감
-> 쓸모 없는 로직이었는지 체크할 것
"""
