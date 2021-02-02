/*
1233. 사칙연산 유효성 검사
210202 Solution

*/

#include <iostream>
#include<cstring>
using namespace std;
int data_set[201][2];
int data_num[201];
char data_chr[201];

bool is_operator(int index) {
    if (data_chr[index] == '\0') return false;
    return true;
}


bool search(int index) {
    if (is_operator(index)) {
        if (data_set[index][0] != 0 && data_set[index][1] != 0) {
            if (search(data_set[index][0]) && search(data_set[index][1])) return true;
        }
        return false;
    }
    else {
        if (data_set[index][0] != 0 || data_set[index][1] != 0) return false;
        return true;
    }
}



int main()
{
    int tc_num, length;

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        memset(data_set, 0, sizeof(data_set));
        memset(data_num, 0, sizeof(data_num));
        memset(data_chr, '\0', sizeof(data_chr));
        cin >> length;
        for (int i = 1; i <= length; i++) {
            int index;
            char chr;
            cin >> index;
            cin.ignore();
            chr = cin.peek();
            if (chr >= '0' && chr <= '9') {
                int value;
                cin >> value;
                data_num[index] = value;
            }
            else {
                cin >> chr;
                data_chr[index] = chr;
            }
            if (length >= 2 * index) {
                cin >> data_set[index][0];
            }
            if (length >= 2 * index + 1) {
                cin >> data_set[index][1];
            }
        }
        cout << "#" << tc_num << " " << search(1) << endl;

    }
    return 0;
}
