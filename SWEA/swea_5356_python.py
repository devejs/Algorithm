"""
5356. 의석이의 세로로 말해요
210225 Solution
1. 문자열을 받아올 때 문자열 리스트와 리스트의 길이 배열을 같이 생성한다.
2. 가장 긴 길이만큼 반복문을 돈다.
3. 반복문 안에서 문자열 리스트를 돌면서 길이가 인덱스보다 큰 것만 결과에 추가한다.
"""

tc = int(input())
for tc in range(1,tc+1):
    str_lines = []
    str_length = []
    results = []
    for i in range(5):
        str_lines.append(list(input()))
        str_length.append(len(str_lines[i]))
    for i in range(max(str_length)):
        for s in str_lines:
            if len(s) > i:
                results.append(s[i])

    print(f"#{tc} {''.join(results)}")