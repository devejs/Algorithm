"""
2822. 점수 계산
210202 Solution
1. 문제 번호를 기억하기 위해 인덱스와 점수를 튜플로 같이 저장
2. 튜플의 두번째 요소인 점수를 기준으로 내림차순 정렬
3. 앞에서부터 5개 돌면서 합 구하고 추가 리스트에 각 문제 번호 저장
4. 문제 번호는 오름차순으로 정렬
"""

scores = []
sum = 0
strList = []
for i in range(8):
    score = int(input())
    scores.append((i,score))
scores.sort(key=lambda x:x[1], reverse=True)
for index, score in scores[:5]:
    sum += score
    strList.append(str(index+1))
strList.sort()
print(sum)
print(" ".join(strList))
