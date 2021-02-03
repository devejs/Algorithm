/*
1242. 암호코드 스캔
210203 Solution
1. 암호 코드가 여러개이므로 어디에 있는지 알 수 없어 1~N-1까지 완전탐색
2. 16진수는 바로 2진수로 바꿔서 배열에 넣어줌
3. 1240과 마찬가지로 첫번째 1을 찾아 암호코드의 길이를 구하되, 숫자 1개만 먼저 구해서 비율(ratio)을 구함
4. 비율을 구하기 위해서 나온 0,1,0,1 비율로 바로 10진수 암호 값을 구해줌
5. 4에서 구한 값을 배열에 넣어 배열의 길이가 8일 때 암호 검증
*/

#include <iostream>
#include <cstring>
using namespace std;

int code_ratio[][4] = {
    {3,2,1,1},
    {2,2,2,1},
    {2,1,2,2},
    {1,4,1,1},
    {1,1,3,2},
    {1,2,3,1},
    {1,1,1,4},
    {1,3,1,2},
    {1,2,1,3},
    {3,1,1,2}
};
int hex_to_bin[][4] = {
    {0,0,0,0},
    {0,0,0,1},
    {0,0,1,0},
    {0,0,1,1},
    {0,1,0,0},
    {0,1,0,1},
    {0,1,1,0},
    {0,1,1,1},
    {1,0,0,0},
    {1,0,0,1},
    {1,0,1,0},
    {1,0,1,1},
    {1,1,0,0},
    {1,1,0,1},
    {1,1,1,0},
    {1,1,1,1}
};

int dec_code[8] = { 0, };
int data_set[2000][2000] = { 0, };
bool visited[2000][2000] = { false, };

int hexToBin(char h) {
    if (h <= '9') return h - '0';
    return h - 'A' + 10;
}

int gcd(int a, int b) {
    // a>=b
    if (b > a){
        int temp = a;
        a = b;
        b = temp;
    }
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int arr_equal(int* arr, int ratio) {
    bool flag = false;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 4; j++) {
            if (code_ratio[i][j]*ratio != arr[j]) break;
            if (j == 3) flag = true;
        }
        if (flag) return i;
    }
}

int find_range(int x, int y) {
    int count[4] = { 0, };
    int x_index = x;
    int y_index = y;
    int length;
    int ratio;
    for (int i = 1; i < 4; i++) {
        int value = i % 2;
        while (data_set[y][x_index] == value) {
            count[i]++;
            x_index++;
        }
    }
    while (data_set[y_index][x] == 1) {
        y_index++;
    }

    length = x_index - x;
    if (length > 7) {
        ratio = gcd(gcd(count[1], count[2]), count[3]);
        count[0] = (7 - (count[1] + count[2] + count[3]) / ratio)*ratio;
    }
    else {
        count[0] = 7 - (length % 7);
        ratio = 1;
    }

    for (int i = y; i < y_index; i++) {
        for (int j = x - count[0]; j < x_index; j++) {
            visited[i][j] = true;
        }
    }
    return arr_equal(count, ratio);
}

int check_code(int* arr) {
    int od_sum = 0;
    int ev_sum = 0;
    for (int i = 0; i < 8; i++) {
        if (i % 2 == 0) {
            od_sum += dec_code[i];
        }
        else {
            ev_sum += dec_code[i];
        }
    }
    int result = 0;
    if ((od_sum * 3 + ev_sum) % 10 == 0) {
        return (od_sum + ev_sum);
    }
    else {
        return 0;
    }
}

int main()
{
    int tc;

    cin >> tc;
    for (int tc_num = 1; tc_num <= tc; tc_num++) {
        memset(dec_code, 0, sizeof(dec_code));
        memset(data_set, 0, sizeof(data_set));
        memset(visited, false, sizeof(visited));

        int result = 0;
        int row, col;
        char hex_arr[501] = { '\0', };
        char hex_chr;
        cin >> col;
        cin >> row;
        for (int i = 0; i < col; i++) {
            cin >> hex_arr;
            int tmp_id = 0;
            int j = 0;
            while (hex_arr[tmp_id] != '\0') {
                int index = hexToBin(hex_arr[tmp_id++]);
                for (int e = 0; e < 4; e++) {
                    data_set[i][j + e] = hex_to_bin[index][e];
                }
                j += 4;

            }
        }
        int index = 0;
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row * 4; j++) {
                if (data_set[i][j] == 1 && !visited[i][j]) {
                    dec_code[index++] = find_range(j, i);
                    if (index == 8) {
                        index = 0;
                        result += check_code(dec_code);
                    }
                }
            }
        }
        cout << "#" << tc_num << " " << result << endl;
    }
}

/*
1240 문제와 다르게 어려웠던 점
1. 코드가 여러 개임; 어디서 코드가 시작하는지도 알기 쉽지 않음
2. 코드 길이가 56으로 고정이 아니라 56의 배수가 됨. 해당 비율을 알아내기 어려웠음

삽질 기록
0. 처음에 16진수를 기준으로 암호코드를 분리하려고 했다가 실패(16진수가 무조건 14개 배수가 아님)
1. 포인트 구조체를 만들어 암호코드 덩어리의 시작점, 끝점을 기록했는데 코드 길이를 깜빡하고 코드의 숫자 1개 단위로 큐에 넣어버림
2. 1번은 사실 큰 문제가 아니었는데 포인트 구조체, 구조체 넣는 큐, 뭐 이것저것 쓸데없이 길게 코드를 짜서 런타임 에러 발생(swea에서만)
3. 가장 큰 핵심 문제가 됐던 것-> 비율 알고리즘 잘못 짬; ratio = 1일때 기준으로 count[0]을 계산해서 ratio >=2 되자마자 다 엉망
*/
