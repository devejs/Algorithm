"""
1208. Flatten
210125 Solution
1. 배열 sort
2. count만큼 반복
3-1.배열[0]+= 1, 배열[-1]-=1
3-2. 다시 sort
4. max-min <=1 이면 반복 중단
"""

for i in range(10):
    num= int(input())
    boxed = list(map(int, input().split()))
    boxed.sort()
    count = 0
    while (count < num):
        count += 1
        boxed[0] += 1
        boxed[-1] -= 1
        if max(boxed) - min(boxed) == 1 or max(boxed) - min(boxed) == 0:
            break
        else:
            boxed.sort()
    print(f"#{i+1} {max(boxed)-min(boxed)}")


"""
실패했던 알고리즘(시간 초과)
for range(count):
        max(boxed) -= 1
        min(boxed) += 1

-> 불필요한 횟수 반복
-> for(O(n))에 max/min 시간복잡도
"""
