/*
1234. 계산기3
210129 Solution
1. 빈 스택에 비밀번호를 하나씩 넣어줌
2. 스택의 마지막 인자와 넣는 인자를 비교하며 pop or push
*/

#include <iostream>
using namespace std;

int is_empty_arr(int *arr){
    if(arr[0] == -1) return 1;
    return 0;
}

int main(){
    int length;
    char numbers[100];
    int password[100];
    int top;

    for (int tc_num =1; tc_num <= 10; tc_num++){
        cin >> length;
        cin >> numbers;
        fill_n(password, 100, -1);
        top = -1;

        for (int i=0; i<length; i++){
            if (is_empty_arr(password) && top < 0){
                password[++top] = numbers[i] - '0';
            }else{
                if (password[top] == numbers[i] - '0'){
                    password[top--] = -1;
                }else{
                    password[++top] = numbers[i] - '0';
                }
            }
        }
        cout << "#" << tc_num << " ";
        for (int j=0; j<=top; j++){
            cout << password[j];
        }
        cout << endl;
    }
}
