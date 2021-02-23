"""
1244. 스위치 켜고 끄기
1. 인덱싱 편하게 하려고 그냥 임의로 마진 인덱스 0(-1)을 추가해줌.
2. 남학생은 단순히 배수일 때마다(나머지 0) 스위칭
3. 여학생은 먼저 지정된 숫자를 기준으로 왼쪽과 오른쪽 더 짧은 길이를 구해줌(대칭 비교 횟수)
4. 3에서 구한 횟수만큼 반복하되 대칭이 아니면 바로 break
5. 대칭이면 새 리스트에 인덱스를 넣어 반복 종료 후 해당 인덱스 스위칭
인덱스 길이나 이런 별로 쓸데없는 자잘한 거에서 실수를 해서 디버깅하는 데 오래 걸림. 처음에 print 찍어가면서 확인할 것
"""
def boy(num):
    for i in range(sw_num+1):
        if i % num == 0:
            print(switch)
            switch[i] = 0 if switch[i] else 1
            print(switch)

def girl(num):
    left = num - 1 if num <= len(switch) - num else len(switch) - num - 1
    change = [num]
    if left:
        for i in range(1, left + 1):
            if switch[num - i] == switch[num + i]:
                change.extend([num - i, num + i])
            else:
                break
    print(change)
    for i in change:
        switch[i] = 0 if switch[i] else 1
        print(switch)

sw_num = int(input())
switch = [-1]
switch.extend(list(map(int,input().split())))
st_num = int(input())
students = []
for i in range(st_num):
    a, b =map(int, input().split())
    students.append((a,b))

for gender, num in students:
    if gender == 1:
        boy(num)
    else:
        girl(num)

switch = switch[1:]
quot = len(switch) // 20
remain = len(switch) % 20
for i in range(quot):
    for s in switch[i*20:(i+1)*20]:
        print(s, end=' ')
    print()
if remain:
    for s in switch[quot*20:]:
        print(s, end=' ')