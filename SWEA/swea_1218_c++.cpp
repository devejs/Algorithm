/*
1218. 괄호 짝짓기
210128 Solution
1. 괄호 아스키 코드 확인
2. 스택이 비어있으면 문자를 넣고, 스택이 차 있으면 문자를 비교한다.
3. 짝이 안 맞으면 스택에 넣고, 문자가 끝났는데도 스택이 차 있으면 false
4. 문자를 비교하거나 스택이 비어있는 함수는 따로 구현
*/

#include <iostream>
using namespace std;

int is_pair(char left, char right){
    if (right - left == 1 or right - left == 2) return 1;
    return 0;
}

int is_empty_arr(char *arr){
    if (arr[0] == '\0') return 1;
    return 0;
}

int main(){
    int length, tc_num, top;
    bool result;
    char tc_str[1000];
    // char unchecked_stack[500];

    for (tc_num = 1; tc_num <= 10; tc_num++){
        cin >> length;
        cin >> tc_str;
        char unchecked_stack[500] = {'\0',};
        result = true;
        top = -1;
        for (int index=0; index < length; index++){
            if (is_empty_arr(unchecked_stack)){
                unchecked_stack[0] = tc_str[index];
                top = 0;
            }else{
                if (is_pair(unchecked_stack[top], tc_str[index])){
                    // pop
                    unchecked_stack[top] = '\0';
                    top--;
                }else{
                    unchecked_stack[++top] = tc_str[index];
                }
            }
        }
        if (!is_empty_arr(unchecked_stack)) result = false;
        cout << "#" << tc_num << " " << result << endl;
    }
    return 0;
}
