"""
1974. 스도쿠 검증
210225 Solution
1. 가로, 세로, 3*3 박스로 나누어 합을 계산한다.
2. 합이 45가 아니면 result = 0, break
"""

VALUE = 45
tc = int(input())
for tc in range(1, tc+1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    result = 1
    col = [0]*9
    square = [0]*3

    for index, row in enumerate(sudoku):
        # 가로
        if sum(row) != VALUE:
            result = 0
            break
        # 박스
        for i in range(3):
            square[i] += sum(row[3*i:3*(i+1)])
        if index % 3 == 2:
            for i in square:
                if i != VALUE:
                    result = 0
                    break
            else:
                square = [0]*3
        # 세로
        for j in range(9):
            col[j] += row[j]

    for i in col:
        if i != VALUE:
            result = 0
            break
    print(f"#{tc} {result}")

"""
빠지기 쉬운 함정
배열에 든 여러 열/박스의 합을 싸잡아서 계산하면 반례가 생김
"""