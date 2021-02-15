"""
2659. 십자카드 문제
210215 Solution
1. 가장 작은 시계수(1111)부터 1씩 증가
2. 시계수가 가능한지 확인
3. 시계수를 구하고 인풋보다 작을 경우 카운트++
"""
nums = list(input().split())

def get_clock(nums):
    numbers = []
    if '0' in nums:
        return -1
    for _ in range(4):
        nums.append(nums.pop(0))
        numbers.append(''.join(nums))
    return int(min(numbers))

crit = 1111
count = 1
clock = get_clock(nums)

while crit != clock:
    crit += 1
    temp = list(str(crit))
    if get_clock(temp) == crit:
        count += 1

print(count)
