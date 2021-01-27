"""
1220. Magnetic
210126 Solution
1. 전치행렬 구함
2. for문으로 1,2 값만 빼냄
3. 1의 값은 스택에 담고 2일때 count++
"""

for tc_num in range(10):
    rec_len = int(input())
    arr = [[] for _ in range(rec_len)]
    N = "1"
    S = "2"
    for i in range(rec_len):
        for index, num in enumerate(input().split()):
            arr[index].append(num)

    count = 0
    for array in arr:
        value_list = []
        for num in array:
            if num == N:
                value_list.append(num)
            elif num == S:
                if len(value_list):
                    value_list = []
                    count += 1
    print(f"#{tc_num+1} {count}")


"""
삽질 기록
1. 일일이 다 swap하려고 시도함
2. 한 줄 끝날 때 value_list 초기화 안해줌
"""
