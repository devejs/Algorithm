"""
2605. 줄 세우기
1. 최종 위치는 원래 위치(인덱스)-이동할 위치(인풋)
"""
num = int(input())
students = list(map(int,input().split()))
line = []
for i in range(num):
    line.insert(i-students[i], i+1)
for i in line:
    print(i, end=' ')