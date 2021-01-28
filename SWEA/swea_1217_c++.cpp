/*
1217. 거듭제곱
210128 Solution
재귀함수로 구현
*/
#include <iostream>
using namespace std;

int get_square(int base, int power){
    if (power > 0) { return base * get_square(base, power-1); }
    return 1;
}

int main(){
    int tc_num, base, power;

    for (int tc_num = 1; tc_num <= 10; tc_num++){
        cin >> tc_num;
        cin >> base;
        cin >> power;

        cout << "#" << tc_num << " " << get_square(base, power) << endl;
    }


    return 0;
}
