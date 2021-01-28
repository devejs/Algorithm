/*
1215. 회문1
210127 Solution
1. 찾을 회문 길이로 반복 구간 설정
2. 문자열 끝에 도달할 때까지 반복하며 count++, 행과 열 모두 반복
*/

#include <iostream>
using namespace std;


int main() {
    int tc_num, palindrome_len, count;
    char table[8][8];

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        cin >> palindrome_len;
        for (int i = 0; i < 8; i++) {
            cin >> table[i];
        }
        count = 0;

        for (int row = 0; row < 8; row++) {
            int index = 0;
            int end_index = index + palindrome_len - 1;
            while (end_index < 8) {
                int rep_num = palindrome_len / 2 + palindrome_len % 2;
                for (int repeat = 0; repeat < rep_num; repeat++) {
                    if (table[row][index+repeat] != table[row][end_index-repeat]) break;
                    if (repeat == rep_num - 1) {
                        count++;
                    }
                }
                index++;
                end_index++;
            }
        }

        for (int col = 0; col < 8; col++) {
            int index = 0;
            int end_index = index + palindrome_len - 1;
            while (end_index < 8) {
                int rep_num = palindrome_len / 2 + palindrome_len % 2;
                for (int repeat = 0; repeat < rep_num; repeat++) {
                    if (table[index+repeat][col] != table[end_index - repeat][col]) break;
                    if (repeat == rep_num - 1) {
                        count++;
                    }
                }
                index++;
                end_index++;
            }
        }
        cout << "#" << tc_num << " " << count << endl;
    }
    return 0;
}
