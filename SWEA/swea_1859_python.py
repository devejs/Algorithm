"""
1859. 백만장자 프로젝트
210222 Solution
1. 뒤에서부터 세기 위해 배열 reverse (뒤에서부터 세는 이유는 아래에)
2. 반복으로 배열을 돌되 항상 그 다음 원소와 비교하므로 반복 길이는 length-1
3. 기준점을 두고 다음 원소와 비교하되 다음 원소가 작으면 차를 더해주고, 크면 기준점을 바꿔준다.
"""

tc = int(input())
for tc in range(1, tc+1):
    days = int(input())
    prices = list(map(int,input().split()))[::-1]
    earning = 0
    cric = prices[0]
    for i in range(len(prices)-1):
        if cric >= prices[i+1]:
            earning += cric-prices[i+1]
        else:
            cric = prices[i+1]

    print(f"#{tc} {earning}")


"""
처음에는 단순하게 앞에서부터 최댓값을 찾아 해당 최댓값 전까지 값을 더하는 식으로 풀이했다.
이랬더니 값은 맞았지만 TC 7번부터 시간 초과가 심하게 났다. 케이스가 많아질수록 max값을 구하는 시간이 낭비가 됨.
이러한 문제 류를 뒤에서부터 풀어야하는 이유는 리스트 안에 max 값이 여러 개 있을 경우 중복값이 앞에서 계속 걸리기 때문.
따라서 뒤의 값이 클수록 유리하기 때문에 뒤에서 풀면 훨씬 유리하다.
"""