"""
2007. 패턴 마디의 길이
210222 Solution
1. 문자열 슬라이싱
2. 길이 1부터 1씩 늘려가면서 다음 문자열이 동일한 문자열인지 확인
3. 같은 패턴이 반복되기 때문에 가능한 방식

c++로 i,j 해서 푸는 방법으로 다시 풀어보기
"""
tc = int(input())
for tc in range(tc):
    strs = input()
    length = 1
    for i in range(1, 30):
        if strs[0:i] == strs[i:i*2]:
            length = i
    print(f"#{tc} {length}")