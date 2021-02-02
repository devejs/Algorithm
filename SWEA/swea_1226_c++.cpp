/*
1226. 미로1
210201 Solution
1. 큐 라이브러리 사용
2. 제일 기본적인 큐 BFS(주변 값 확인해서 갈 수 있는 길만 큐에 푸시)
3. 큐를 하나씩 비우면서 갈 수 있는 길이 없을 때까지 반복; 그 전에 목적지를 찾으면 결과 리턴
-> 아무리 해도 TC 7번이 답이 틀림ㅠㅠ
*/

#include <iostream>
#include <queue>
using namespace std;

struct Point {
    int x;
    int y;
};


int main() {
    int tc_num, start_x, start_y;
    int dx[4] = { 0,0,-1,1 }; // 상하좌우
    int dy[4] = { -1, 1, 0, 0 };
    queue<Point> q;

    //FILE* input;
    //freopen_s(&input, "input.txt", "r", stdin);

    for (tc_num = 1; tc_num <= 10; tc_num++) {
        start_x = 0;
        start_y = 0;
        int result = 0;
        int map_data[16][16] = { 0, };
        bool visited[16][16] = { false, };
        char temp_data[17];
        cin >> tc_num;
        for (int i = 0; i < 16; i++) {
            cin >> temp_data;
            cin.get();
            for (int j = 0; j < 16; j++) {
                map_data[i][j] = temp_data[j] - '0';
                if (map_data[i][j] == 2) {
                    start_x = j;
                    start_y = i;
                }
            }
        }
        struct Point p = { start_x, start_y };
        q.push(p);
        visited[start_y][start_x] = true;

        while (!q.empty()) {
            int temp = q.size();
            for (int i = 0; i < temp; i++) {
                int cur_x = q.front().x;
                int cur_y = q.front().y;
                q.pop();
                for (int j = 0; j < 4; j++) {
                    int around_x = cur_x + dx[j];
                    int around_y = cur_y + dy[j];
                    if (around_x > 0 && around_x < 16 && around_y > 0 && around_y < 16  && !visited[around_y][around_x]) {
                        if (map_data[around_y][around_x] == 3) {
                            result = 1;
                            break;
                        }
                        else if (map_data[around_y][around_x] == 0) {
                            map_data[around_y][around_x] = 1;
                            struct Point p = { around_x, around_y };
                            q.push(p);
                            visited[around_y][around_x] = true;
                        }
                    }
                }
                if (result) break;
            }
            if (result) break;
        }
        cout << "#" << tc_num << " " << result << endl;

    }

}
