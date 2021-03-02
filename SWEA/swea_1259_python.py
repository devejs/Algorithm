"""
1259. 금속막대
1. 모든 나사가 한 줄로 맞물린다고 보장되어 있으므로 순서 관계 없이 pop하면서 앞 뒤 찾아주기
2. 더이상 왼쪽/오른쪽에 맞는 나사가 없으면 계속 탐색할 필요가 없으므로 Flag 사용
3. Female/Male 나누어 각각 왼쪽, 오른쪽에 맞는 값을 덧붙여줌
1번이 보장되어있지 않으면 이런 방식은 안 될 듯
1260 문제의 선행문제
"""
tc = int(input())
for tc in range(1, tc+1):
    num = int(input())
    data = list(map(int, input().split()))
    female = []
    male = []
    for i, v in enumerate(data):
        if i % 2 == 0:
            male.append(v)
        else:
            female.append(v)
    connection = [male.pop(), female.pop()]
    left = True
    right = True
    while left or right:
        if left:
            if connection[0] in female:
                index = female.index(connection[0])
                connection.insert(0, female.pop(index))
                connection.insert(0, male.pop(index))
            else:
                left = False
        if right:
            if connection[-1] in male:
                index = male.index(connection[-1])
                connection.append(male.pop(index))
                connection.append(female.pop(index))
            else:
                right = False
    print(f"#{tc}", end=' ')
    for i in connection:
        print(f"{i}", end= ' ')
    print()

