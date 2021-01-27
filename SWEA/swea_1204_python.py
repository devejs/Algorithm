"""
1204. 최빈수 구하기
210125 Solution
1. set() 메소드로 배열에 나타나는 값 구하기
2. for문으로 1번의 집합 원소가 리스트에 포함된 개수 카운트
3. 최빈수를 저장해 최빈수가 같은 값이 있으면 큰 값으로 출력
"""

tc_num = int(input())
for tc in range(tc_num):
    input()
    scores = list(map(int, input().split()))
    set_scores = set(scores)
    max_count = 0
    max_score = 0
    for i in set_scores:
        if max_count < scores.count(i):
            max_count = scores.count(i)
            max_score = i
        elif max_count == scores.count(i):
            max_score = i if i > max_score else max_score
    print(f"#{tc+1} {max_score}")
