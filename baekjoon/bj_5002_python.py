"""
5002. 도어맨
210331 Solution
스택으로 푸는 문젠데 스택 안 씀
1. 각각 여자/남자의 수와 그 차이를 저장한다.
2. 배열의 값을 pop하는 대신(시간 소요) idx로 위치를 표기해준다.
3. 마지막 사람 남은 경우(idx == len(line)-1)나 차이가 없을때는 바로 해당 성별 수 증가
4. 그렇지 않다면 차이에 따라 선호하는 성별을 먼저 입장시키되(증가), 둘다 아닐 경우 맨 앞 사람 입장
5. 차이(dif)가 차이의 최댓값(dif_max)보다 커지면 break
6. 차이가 크지 않더라도 모든 사람이 입장해서 반복문이 종료될 수 있으므로 출력 전 확인해줌
"""

dif_max = int(input())
line = list(input())
dif = 0
# female, male
people = [0,0]
idx = 0
while idx < len(line) and dif <= dif_max:
    if dif == 0 or idx == len(line)-1:
        if line[idx] == 'W':
            people[0] += 1
        else:
            people[1] += 1

    elif people[0]-people[1] > 0:
        # 여자 > 남자 -> 남자를 추가하길 바라
        if line[idx] == 'M':
            people[1] += 1
        elif line[idx+1] == 'M':
            people[1] += 1
            line[idx], line[idx+1] = line[idx+1], line[idx]
        else:
            people[0] += 1

    elif people[0]-people[1] < 0:
        # 남자 > 여자 -> 여자를 추가하길 바라
        if line[idx] == 'W':
            people[0] += 1
        elif line[idx+1] == 'W':
            people[0] += 1
            line[idx], line[idx+1] = line[idx+1], line[idx]
        else:
            people[1] += 1

    idx += 1
    dif = abs(people[0]-people[1])

if dif > dif_max:
    print(sum(people)-1)
else:
    print(sum(people))