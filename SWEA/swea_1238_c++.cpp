/*
1238. Contact
210201 Solution
1. 큐 라이브러리 사용
2. 기본으로 사용할 큐와 마지막 연락값을 알 큐 두 개 사용
3. 큐를 사용한 BFS(출발하는 연락처에서 가능한 모든 연락 돌리기)
4. 매번 연락을 돌리기 전 복사 큐를 비우고 돌린 연락처를 복사 큐에 다시 푸시
5. 모두 방문했으면 큐가 비게 되므로 복사해둔 큐에 있는 연락처 중 최댓값 구하기
*/

#include <iostream>
#include <queue>
using namespace std;


int main() {
    int tc_num, start_num, length;
    queue<int> q;
    queue<int> left;

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        int data_set[101][101] = {0, };
        bool visited[101] = { false, };
        cin >> length;
        cin >> start_num;
        for (int i = 0; i < length / 2; i++) {
            int from, to;
            cin >> from;
            cin >> to;
            data_set[from][to] = 1;
        }
        q.push(start_num);
        visited[start_num] = true;
        while (!q.empty()) {
            int temp = q.size();
            while (!left.empty()) { left.pop(); }
            for (int i = 0; i < temp; i++) {
                int from = q.front();
                left.push(from);
                q.pop();
                for (int j = 0; j < 101; j++) {
                    if (data_set[from][j] == 1 && !visited[j]) {
                        visited[j] = true;
                        q.push(j);
                    }
                }
            }
        }
        int max_value = 0;
        int temp = left.size();
        for (int i = 0; i < temp; i++) {
            if (left.front() > max_value) {
                max_value = left.front();
            }
            left.pop();
        }
        cout << "#" << tc_num << " " << max_value << endl;
    }
    return 0;
}
