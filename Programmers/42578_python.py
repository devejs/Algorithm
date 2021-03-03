"""
프로그래머스 > 해시 > 위장
https://programmers.co.kr/learn/courses/30/lessons/42578
210303 Solution
1. 각 의상의 종류를 딕셔너리에 담아 개수를 카운트
2. 딕셔너리의 키(의상 종류)를 돌면서 해당 의상의 가짓수+1 
3. 가짓수+1 -> 옷을 선택할 수 있는 경우의 수 + 옷을 입지 않는 경우 
4. 
5. 옷을 하나도 입지 않고 있는 경우는 없으므로 최종 개수에서 -1
"""
def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    for i in dict.keys():
        answer *= (dict[i]+1)
    answer -= 1
    return answer