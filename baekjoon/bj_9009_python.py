"""
9009. 피보나치
210407 Solution
1. 피보나치 수 메모이제이션으로 저장(num보다 하나 큰 수까지만)
2. num보다 작으면서 제일 큰 수를 더하되, 합이 num보다 작을때만 누적 합
"""
tc = int(input())
fibo = [0,1]
for _ in range(tc):
    num = int(input())
    k = 1
    ans = []
    while (fibo[k] <= num):
        if k == len(fibo)-1:
            fibo.append(fibo[k]+fibo[k-1])
        else:
            k += 1
    sum = 0
    for v in fibo[::-1]:
        if sum+v < num:
            sum += v
            ans.append(v)
        elif sum+v == num:
            ans.append(v)
            break

    print(*ans[::-1])

"""
이미 문제 카테고리가 그리디라서 뒤에서부터 제일 큰 수를 카운트해도 어떻게든 답이 될거라는 확신이 있었는데, 
만약 문제 유형이 그리디가 아니었다면 풀 수 있었을지 모르겠다
"""