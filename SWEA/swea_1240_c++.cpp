/*
1240. 단순 2진 암호코드
210203 Solution
1. 0은 구별이 불가하므로 암호 코드 시작점(1) 찾기
2. 암호 코드의 끝이 1이므로 0이 나올때까지 길이를 구하기
3. 코드의 총 가로 길이가 56이므로 56-(2번 값)은 찾은 시작점의 앞부분 0
4. 코드를 해석해 10진 배열로 만들고 검증 코드 맞는지 확인
*/
#include <iostream>
using namespace std;
int code_num[][7] = {
    {0,0,0,1,1,0,1},
    {0,0,1,1,0,0,1},
    {0,0,1,0,0,1,1},
    {0,1,1,1,1,0,1},
    {0,1,0,0,0,1,1},
    {0,1,1,0,0,0,1},
    {0,1,0,1,1,1,1},
    {0,1,1,1,0,1,1},
    {0,1,1,0,1,1,1},
    {0,0,0,1,0,1,1}
};

int arr_equal(int *arr) {
    bool flag = false;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 7; j++) {
            if (code_num[i][j] != arr[j]) break;
            if (j == 6) flag = true;
        }
        if (flag) return i;
    }
}

int main()
{
    int tc;

    cin >> tc;
    for (int tc_num=1; tc_num <= tc; tc_num++) {
        int dec_code[8] = { 0, };
        int bin_code[56] = { 0, };
        char data[50][100] = { '\0', };
        int row, col;
        cin >> col;
        cin >> row;
        for (int i = 0; i < col; i++) {
            cin >> data[i];
        }
        // 암호 코드 부분 찾기
        int x = -1;
        int y = -1;
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (data[i][j] == '1') {
                    x = j;
                    y = i;
                    break;
                }
            }
            if (x != -1) break;
        }
        int left = 0;
        while (data[y][x+55-left]=='0' || data[y][x + 55 - left] == '\0') {
            left++;
        }
        // 10진수 코드 찾기
        for (int i = 0; i < 56; i++) {
            bin_code[i] = data[y][x - left+i] - '0';
        }
        int index = 0;
        for (int i = 0; i < 8; i++) {
            int temp_code[7] = { 0, };
            for (int j = 0; j < 7; j++) {
                temp_code[j] = bin_code[index++];
             }
            dec_code[i] = arr_equal(temp_code);
        }
        // 검증코드 확인
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
            result = od_sum + ev_sum;
        }
        cout << "#" << tc_num << " " << result << endl;

    }
}
