"""
1920. 수 찾기
210324 Solution
해시
1. 주어진 정수를 딕셔너리로 저장
2. 구해야 하는 정수들이 딕셔너리에 있으면 1, 없으면 0 출력
"""
n = int(input())
numbers = input().split()
dic = {}
for i in numbers:
    dic[i] = 1

m = int(input())
second = input().split()
for i in second:
    if i in dic:
        print(1)
    else:
        print(0)

"""
Q. 해시 사용하지 않고 그냥 리스트에서 if .. in 으로 찾으면 시간 차이가 얼마나 날까?
"""