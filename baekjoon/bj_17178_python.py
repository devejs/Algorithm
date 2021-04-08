"""
17178. 줄서기
210407 Solution
1. 알파벳과 숫자 분리
2. 줄 순서대로 돌면서 현재 위치 기록
3. 뒷 줄에 현재 위치보다 작은 수가 있으면 대기 스택에 추가, 없으면 다음 위치로
4. 대기 스택에 넣을 때 넣을 수보다 작은 수가 있는지 체크, 마지막 수가 더 작으면 pop 반복
5. 모든 줄이 2~4의 과정을 거쳐 끝에 도달하면 good, 중간에 걸리면 bad 출력하고 return
"""
def is_in(alp, no, arr):
    # arr = (alp, no)
    if arr[0] == alp:
        if arr[1] < no:
            return True
        else:
            return False
    elif arr[0] < alp:
        return True
    else:
        return False

def check(alp, no):
    global line
    for k in range(cur[1], 5):
        if is_in(alp, no, people[cur[0]][k]):
            return False
    for i in range(cur[0]+1, line):
        for j in range(5):
            if is_in(alp, no, people[i][j]):
                return False
    return True

def solve():
    for i, ticket in enumerate(people):
        cur[0] = i
        for j, value in enumerate(ticket):
            cur[1] = j
            alp = value[0]
            no = value[1]
            while len(waiting) > 0:
                if check(waiting[-1][0], waiting[-1][1]):
                        waiting.pop()
                else:
                    break
            if not check(alp, no):
                if len(waiting):
                    for w_alp, w_no in waiting:
                        if w_alp < alp or (w_alp == alp and w_no < no):
                            print("BAD")
                            return
                waiting.append((alp, no))
    print("GOOD")
    return

line = int(input())
people = [[] for _ in range(line)]
waiting = []
cur = [-1,-1]
res = True
for i in range(line):
    temp = input().split()
    for j in range(5):
        alph, no = temp[j].split('-')
        people[i].append((alph, int(no)))

solve()