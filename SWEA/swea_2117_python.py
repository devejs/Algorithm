"""
2117. 홈 방범 서비스
210307 Solution
1. 최대 이익(지도의 모든 1의 개수*회비)일 때 최대인 k의 값을 구해서 1씩 줄여가며 완전탐색
2. 그러나 k의 값이 너무 작아져 구하는 최대 결과값보다 마름모의 범위가 작아질 경우 break (백트래킹)
3. 중점을 기준으로 상하좌우로 (k-1)씩 증감하는 규칙에 따라 해당 마름모 부분에 집이 있으면 count++
4. 손해를 보지 않고, count값이 현재 결과값보다 클 때 결과값 갱신
"""

def cal_k(k):
    return k*k+(k-1)*(k-1)
 
def cal_k_count(k):
    count = 0
    for i in range(2*k-1):
        if i <= k:
            count += 1+2*i
        else:
            count += 1+2*(k-2+(k-i))
    return count
 
tc = int(input())
for tc in range(1,tc+1):
    size, price = map(int, input().split())
    mapp = []
    house_no = 0
    for i in range(size):
        mapp.append(input().split())
        house_no += mapp[i].count('1')
    max_price = price*house_no
    max_k = 1
    while True:
        if cal_k(max_k) > max_price:
            max_k = max_k -1
            break
        else:
            max_k += 1
 
    ans = [1]
    for k in reversed(range(2,max_k+1)):
        # 백트래킹
        if cal_k_count(k) <= ans[0]:
            break
        for i in range(size):
            #col = size-k+1
            for j in range(size):
                # 중점 처리 (i,j)
                count = 1 if mapp[i][j]=='1' else 0
                for r1 in range(k):
                    # r1: 행(상하), r2: 열(좌우)
                    for r2 in range(k-r1):
                        if r1==0:
                            if r2 ==0:
                                continue
                            else:
                                if 0 <= j - r2:
                                    if mapp[i][j - r2] == '1':
                                        count += 1
                                if j + r2 < size:
                                    if mapp[i][j + r2] == '1':
                                        count += 1
                        else:
                            # 위
                            if 0 <= i-r1:
                                if r2 == 0:
                                    if mapp[i-r1][j]=='1':
                                        count += 1
                                else:
                                    if 0<= j-r2:
                                        if mapp[i-r1][j-r2]=='1':
                                            count+=1
                                    if j+r2 < size:
                                        if mapp[i-r1][j+r2]=='1':
                                            count+=1
                            # 아래
                            if i+r1 < size:
                                if r2 == 0:
                                    if mapp[i+r1][j]=='1':
                                        count +=1
                                else:
                                    if 0<= j-r2:
                                        if mapp[i+r1][j-r2]=='1':
                                            count+=1
                                    if j+r2 < size:
                                        if mapp[i+r1][j+r2]=='1':
                                            count+=1
                if ans[0] < count and cal_k(k) <= price*count:
                    ans[0] = count
 
    print(f"#{tc} {ans[0]}")