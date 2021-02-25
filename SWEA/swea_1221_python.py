"""
1221. GNS
210225 Solution
1. 딕셔너리로 값을 매칭
2. 문자열을 돌면서 새 배열에 각 숫자 인덱스의 개수를 ++
3. 배열 돌면서 개수만큼 딕셔너리 키값(문자열) 출력
"""

# import sys
# sys.stdin=open("GNS_test_input.txt","r")

number_data = {"ZRO": 0, "ONE": 1, "TWO":2, "THR":3, "FOR":4,
            "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
tc = int(input())
for _ in range(tc):
    tc_num, length = input().split()
    length = int(length)
    numbers = input().split()
    count_num = [0]*10
    for num in numbers:
        if num in number_data:
            count_num[number_data[num]] += 1
    print(count_num)
    print(tc_num)
    for str_num, num in number_data.items():
        for _ in range(count_num[num]):
            print(str_num, end= ' ')
    print()



