/*
1225. 암호생성기
210201 Solution
1. 원형 큐 구현(푸시, 팝)
2. 팝한 값에 사이클 카운트를 감소시켜 원형 큐에 다시 푸시
3. 0보다 작거나 같으면 종료
*/

#include <iostream>
using namespace std;

int password[9] = { 0, };
int front, rear, qsize = 9;

bool push(int num) {
    if ((rear + 1) % qsize == front) return false;
    rear = (rear + 1) % qsize;
    password[rear] = num;
    return true;
}

int pop() {
    if (front == rear) return 0;
    int temp = password[front];
    front = (front + 1) % qsize;
    return temp;
}

int check_negative() {
    for (int i = 0; i < 9; i++) {
        if (password[i] <= 0) return i + 1;
    }
    return 0;
}

int main() {
    int tc_num, cycle_count;

    //FILE* input;
    //freopen_s(&input, "input.txt", "r", stdin);

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        fill_n(password, 9, 0);
        cin >> tc_num;
        for (int index = 0; index < 8; index++) {
            cin >> password[index];
        }
        front = 0;
        rear = 7;
        cycle_count = 1;

        while (true) {
            if (cycle_count == 6) cycle_count = 1;
            int temp = pop() - cycle_count;
            push(temp);
            if (temp <= 0) break;
            cycle_count++;

        }

        cout << "#" << tc_num << " ";
        for (int i=0; i<8; i++) {
            int temp = pop();
            if (temp < 0) {
                cout << "0" << " ";
            }
            else {
                cout << temp << " ";
            }
        }
        cout << endl;

    }
}
