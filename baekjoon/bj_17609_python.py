"""
17609. 회문
210331 Solution
1. 첫번째, 마지막 인덱스로부터 같은지 검사
2. 다를 경우 그 앞 문자 검사
3. 2번에 같은 문자가 있으면 유사 회문일 가능성이 있으므로 pal 값을 저장해 큐에 넣기
4. 큐가 빌 때까지 반복
5. 3번의 경우의 수에 따라 pal 값이 여거 개 나올 수 있으므로 이 경우는 1이 맞다.
"""

n = int(input())
inputs = []
# (idx, pal, string)
result = [[] for _ in range(n)]
for i in range(n):
    inputs.append((i, 0, input()))
while len(inputs):
    idx, pal, s = inputs.pop(0)
    first = 0
    last = len(s) - 1
    while (pal < 2 and first <= last):
        if (s[first] == s[last]):
            first += 1
            last -= 1
        else:
            if pal == 1:
                pal += 1
                break
            else:
                new = (s[first + 1], s[last - 1])
                if s[first] in new and s[last] in new:
                    inputs.append((idx, pal+1, s[first:last]))
                    inputs.append((idx, pal+1, s[first+1:last+1]))
                    break
                elif s[first] in new:
                    last -= 1
                    pal += 1
                elif s[last] in new:
                    first += 1
                    pal += 1
                else:
                    pal += 2

    result[idx].append(pal)

for i in result:
    if len(i) == 1:
        print(i[0])
    else:
        if 1 in i:
            print(1)
        else:
            print(2)