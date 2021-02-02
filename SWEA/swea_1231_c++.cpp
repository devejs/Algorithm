/*
1231. 중위순회
210202 Solution

*/

#include <iostream>
#include<cstring>
using namespace std;
int data_set[101][2];
char data_chr[101];

void search(int index) {
    if (data_set[index][0] != 0) {
        search(data_set[index][0]);
    }
    else {
        cout << data_chr[index];
        return;
    }
    cout << data_chr[index];
    if (data_set[index][1] != 0) {
        search(data_set[index][1]);
    }
}

int main()
{
    int tc_num, length;

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        memset(data_set, 0, sizeof(data_set));
        memset(data_chr, '\0', sizeof(data_chr));
        cin >> length;
        for (int i = 1; i <= length; i++) {
            int index;
            cin >> index;
            cin >> data_chr[index];
            if (length >= 2 * index) {
                cin >> data_set[index][0];
            }
            if (length >= 2 * index + 1) {
                cin >> data_set[index][1];
            }
        }
        cout << "#" << tc_num << " ";
        search(1);
        cout << endl;

    }
    return 0;
}
