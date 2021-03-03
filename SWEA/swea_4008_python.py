"""
4008. 숫자 만들기
210303 Solution
1. 백준 연산자 끼워넣기 문제, dfs
"""

def calc(num1, op, num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    else:
        return int(num1/num2)


def dfs(depth, value):
    if depth == len(numbers)-1:
        result.append(value)

    for i in range(4):
        if oper_num[i] > 0:
            oper_num[i] -= 1
            new_v = calc(value, operators[i], numbers[depth+1])
            dfs(depth+1, new_v)
            oper_num[i] += 1


import sys
sys.stdin = open("sample_input.txt","r")
operators = ['+','-','*','/']
tc= int(input())
for tc in range(1, tc+1):
    n = int(input())
    oper_num = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    result = []
    dfs(0, numbers[0])

    print(f"#{tc} {max(result)- min(result)}")


