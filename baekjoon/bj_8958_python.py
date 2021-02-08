"""
8958. OX퀴즈
210208 Solution
1. 선형 배열 완전탐색
2. O를 만날 때마다 count++
"""
tc = int(input())
conclusion = []
scores = []
count = 0
for i in range(tc):
    conclusion.append(list(input()))
    scores.append(0)

for i in range(tc):
    count = 0
    for c in conclusion[i]:
        if c == 'O':
            count += 1
            scores[i] += count
        else:
            count = 0
    print(scores[i])
