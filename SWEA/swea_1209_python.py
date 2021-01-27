"""
1209. Sum
210126 Solution
1. max(row 합)
2. 2중 for- max(열 합)
3. 2중 for- max(대각선 합)
4. 1,2,3중 최댓값
"""

for _ in range(10):
    arr = []
    tc_num = int(input())
    for i in range(100):
        arr.append(list(map(int, input().split())))
    # row max
    row_sum_max = max([sum(row) for row in arr])
    # col max
    col_sum_list = []
    for i in range(100):
        col_sum = 0
        for row in arr:
            col_sum += row[i]
        col_sum_list.append(col_sum)
    col_sum_max = max(col_sum_list)
    # dia max
    dia_right_sum = 0
    dia_left_sum = 0
    for i in range(100):
        dia_right_sum += arr[i][i]
        dia_left_sum += arr[i][99-i]
    print(f"#{tc_num} {max(row_sum_max, col_sum_max, dia_right_sum, dia_left_sum)}")
