/*
1232. 사칙연산
210202 Solution

*/
#include <iostream>
#include<cstring>
using namespace std;
int data_set[1001][2];
int data_num[1001];
char data_chr[1001];
//char operators = { '+','-','*', '/' };

bool is_operator(int index) {
    if (data_chr[index] == '\0') return false;
    return true;
}

float calculate(int index) {
    if (is_operator(index)) {
        switch (data_chr[index]) {
        case '+':
            return calculate(data_set[index][0]) + calculate(data_set[index][1]);
        case '-':
            return calculate(data_set[index][0]) - calculate(data_set[index][1]);
        case '*':
            return calculate(data_set[index][0]) * calculate(data_set[index][1]);
        case '/':
            return calculate(data_set[index][0]) / calculate(data_set[index][1]);
        }
    }
    else {
        return data_num[index];
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
                int left, right;
                cin >> left;
                cin >> right;
                data_chr[index] = chr;
                data_set[index][0] = left;
                data_set[index][1] = right;
            }

        }
        cout << "#" << tc_num << " " << int(calculate(1)) << endl;

    }
    return 0;
}
