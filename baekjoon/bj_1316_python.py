"""
1316. 그룹 단어 체커
210125 Solution
1. 스택에 동일한 알파벳이 없으면 추가
2. 스택에 동일한 알파벳이 있으면 마지막인지 확인
3. 마지막 알파벳이 아니면 떨어져 있으므로 그룹 단어가 아님
"""
tc_num = int(input())
count = 0
for _ in range(tc_num):
    flag = True
    word = input()
    group_list = []
    for w in word:
        if len(group_list) and w in group_list:
            if group_list[-1] != w:
                flag = False
                break
        else:
            group_list.append(w)
    if flag:
        count += 1
print(count)
