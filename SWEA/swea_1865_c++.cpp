/*
1865. 동철이의 일 분배
210205 Solution
1. 행마다 하나씩 선택하되, 해당 열이 중복되면 안됨; 즉, 순열
2. 완전탐색할 경우 열이 중복되기 때문에 중복되지 않는 조건 걸어줌(checked)
3. 리프 노드(count == emp_no)탐색 후 확률값을 결과와 비교해 저장해줌
4. (중요) 수의 조합이 워낙 크기 때문에 시간 초과 방지를 위해 조건문 추가(product <= result)
  1 이하인 실수의 곱셈이므로 값을 곱할수록 작아짐 -> 값을 곱해줄 때 이미 값이 결과보다 작으면 return
*/
#include <iostream>
#include <cstring>
using namespace std;

bool checked[17] = { false, }; // 몇번째 일
int emp_work[17][17] = { 0, };
int emp_no;
double result;

void dfs(double product, int person, int count) {
    if (count == emp_no) {
        if (product > result) result = product;
    }
        for (int j = 0; j < emp_no; j++) {
            if (product <= result) {
                // result product < result 한거랑 시간 차이가 엄청 남 와
                return;
            }
            if (!checked[j]) {
                double temp = (double)emp_work[person][j] / 100.0;
                double new_product = product * temp;
                checked[j] = true;
                dfs(new_product, person+1, count+1);
                checked[j] = false;
            }
        }
}
int main(){

    int tc;
    cin >> tc;
    for (int tc_num = 1; tc_num <= tc; tc_num++) {
        memset(checked, false, sizeof(checked));
        memset(emp_work, 0, sizeof(emp_work));
        result = 0;

        cin >> emp_no;
        for (int i = 0; i < emp_no; i++) {
            for (int j = 0; j < emp_no; j++) {
                cin >> emp_work[i][j];
            }
        }

        for (int i = 0; i < emp_no; i++) {
            dfs(1, i, 0);
        }
        cout << fixed;
        cout.precision(6);
        cout << "#" << tc_num << " " << result*100 << endl;
   }
}
