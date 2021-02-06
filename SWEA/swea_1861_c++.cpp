/*
1861. 정사각형 방
210205 Solution
1. 상하좌우 탐색이므로 BFS
2. 큐, 방문 체크
*/
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

struct Point {
    int x;
    int y;
};

bool checked[1001][1001] = { false, }; // 몇번째 일
int room[1001][1001] = { 0, };
int dx[4] = {1, 0, -1, 0}; // 시계방향; 우, 하, 좌, 상
int dy[4] = {0, 1, 0, -1};
int room_len;
int result[2] = { 0, 0};
queue<Point> room_q;

void bfs(int x, int y, int move, int first) {
        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];
            if (xx >= 1 && xx <= room_len && yy >= 1 && yy <= room_len) {
                if (room[yy][xx] == room[y][x] + 1) {
                    bfs(xx, yy, move + 1, first);
                }
                else {
                    if (move > result[1]) {
                        result[0] = first;
                        result[1] = move;
                    }
                    else if (move == result[1] && first < result[0]) result[0] = first;
                    if (!checked[yy][xx]) {
                        struct Point p = { xx, yy };
                        checked[yy][xx] = true;
                        room_q.push(p);
                    }
                }
            }
        }
}

int main() {
    int tc;
    cin >> tc;
    for (int tc_num = 1; tc_num <= tc; tc_num++) {
        memset(checked, false, sizeof(checked));
        memset(room, 0, sizeof(room));
        memset(result, 0, sizeof(result));

        cin >> room_len;
        for (int i = 1; i <= room_len; i++) {
            for (int j = 1; j <= room_len; j++) {
                cin >> room[i][j];
            }
        }
        struct Point p = { 1,1 };
        checked[1][1] = true;
        room_q.push(p);
        while (!room_q.empty()) {
            int x = room_q.front().x;
            int y = room_q.front().y;
            room_q.pop();
            bfs(x, y, 1, room[y][x]);
        }
        cout << "#" << tc_num << " " << result[0] << " " << result[1] << endl;

    }

}
