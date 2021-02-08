"""
1009. 분산 처리
210125 Solution
1.
"""

tc_num = int(input())
for _ in range(tc_num):
    a, b = input().split()
    int_a = int(a)
    int_b = int(b)
    left_list = []
    for multiplier in range(1, int_b+1):
        if int_a % 10 == 0:
            left_list.append("10")
            break
        left = str(int_a ** multiplier)[-1]
        if left in left_list:
            break
        else:
            left_list.append(left)
    index = int_b % len(left_list)

    if index == 0 or left_list[0] == "10":
        print(left_list[-1])
    else:
        print(left_list[index-1])
