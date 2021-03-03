"""
프로그래머스 > 그리디 > 체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
210303 Solution
1. 여벌의 옷을 가지고 있는 학생 중 분실한 학생이 있으므로 중복 번호를 제거하고, 새로운 여벌옷 학생 배열을 만든다.
2. 분실한 학생 배열을 돌면서 전후 학생이 여벌옷이 있는지 보고, 있으면 여벌옷 배열에서 제거해준다.
3. 옷이 없는 수는 처음 lost의 길이에서, 옷을 빌릴 때마다 --
4. 체육 수업을 들을 수 있는 학생의 수는 전체 수 - 옷이 없는 수
"""

def solution(n, lost, reserve):
    reserve_final = []
    for i in reserve:
        if i in lost:
            lost.remove(i)
        else:
            reserve_final.append(i)
    absence = len(lost)
    for i in lost:
        # if i in reserve:
        #     reserve.remove(i)
        if i-1 in reserve_final:
            absence -= 1
            reserve_final.remove(i-1)
        elif i+1 in reserve_final:
            absence -= 1
            reserve_final.remove(i+1)
    answer = n-absence
    return answer

    """
    처음엔 reverse_final 배열 없이 바로 lost와 reverse_final의 공통된 값을 제하는 식으로 갔는데,
    이렇게 되면 for문 안에서 해당 배열의 값을 remove 하게되므로 포문이 제대로 동작하지 않는다
    """