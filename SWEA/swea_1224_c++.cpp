/*
1224. 계산기3
210129 Solution
1. 중위표기-> 후위표기; 단, 스택에 후위표기 변환을 넣지 않고 중간에 계산
2. 연산자 우선순위가 높거나 같은 연산자가 스택에 있으면 pop하고 Push
3. 닫는 괄호는 짝을 찾아주고, 여는 괄호는 가장 높은 우선순위로 push하되 pop할땐 제일 낮음
*/

#include <iostream>
using namespace std;

char operators[4] = {'(', ')', '+', '*',};

int is_operator(char chr1){
    for (int i=0; i<4; i++){
        if (chr1 == operators[i]) return i+1;
    }
    return 0;
}

int calculate(int a, int b, char op){
    if (op == '+'){
        return a+b;
    }else {
        return a*b;
    }
}

int get_length(char *arr){
    int index = 0;
    while (arr[index] != '\0'){
        index++;
    }
    return index;
}


int main(){
    int length, op_top, result_top;
    char expression[1000];

    // FILE* input;
    // freopen_s(&input, "input.txt", "r", stdin);

    for (int tc_num = 1; tc_num <= 10; tc_num++){
        cin >> length;
        cin >> expression;
        char op_stack[1000] = {'\0', };
        int result[1000] = {0, };
        op_top = -1; result_top = -1;
        int cal_result = 0;

        for (int index=0; index < length; index++){
            switch (is_operator(expression[index])){
                case 1:
                    op_stack[++op_top] = expression[index];
                    break;
                case 2:
                    while (op_top >= 0 && result_top >=1 && op_stack[op_top] != operators[0]){
                        cal_result = calculate(result[result_top--],result[result_top--],op_stack[op_top--]);
                        result[++result_top] = cal_result;
                    }
                    op_top--;
                    break;
                case 3:
                    while (op_top >= 0 && result_top >=1 && op_stack[op_top] - expression[index] >= -1){
                        cal_result = calculate(result[result_top--],result[result_top--],op_stack[op_top--]);
                        result[++result_top] = cal_result;
                    }
                    op_stack[++op_top] = expression[index];
                    break;
                case 4:
                    op_stack[++op_top] = expression[index];
                    break;
                default:
                    result[++result_top] = expression[index] - '0';
            }
        }
        while (op_top >= 0 && result_top >=1){
            cal_result = calculate(result[result_top--],result[result_top--],op_stack[op_top--]);
            result[++result_top] = cal_result;
        }
        cout << "#" << tc_num << " " << result[0] << endl;
    }
}
