/*
3190. 뱀
210502 Solution
1. 사과와 뱀을 알 수 있는 전체 맵, 방향 전환을 알 수 있는 방향 배열을 선언한다.
2. 뱀의 몸을 큐에 넣되, 머리를 큐 뒤에 추가한다.
3. 전체 맵에서 사과(9)가 있으면 continue; 전체 맵에서 사과가 없으면 큐의 첫번째 요소(꼬리)를 팝해준다.
4. 벽에 부딪히거나 전체 맵에서 본인(1) 몸과 만나면 그 때의 시간초를 리턴
*/
#include <iostream>
#include <utility>
#include <queue>
using namespace std;

#define right 0
#define down 1
#define left 2
#define up 3

int n, k, L;
int mapp[101][101] = { 0, };
char dir[10001] = { '\0' };
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
queue<pair<int,int> > snake;
int cur_d = right;

int chdir(int t) {
	if (dir[t] == 'D') return (cur_d + 1) % 4;
	else if (dir[t] == 'L') {
		if (cur_d == 0) return 3;
		else return cur_d - 1;
	}
	else return cur_d;
}

int move() {
	int t = 0;
	snake.push(make_pair(1, 1));
	mapp[1][1] = 1;
	while (1) {
		t++;
		int y = snake.back().first;
		int x = snake.back().second;
		int yy = y + dy[cur_d];
		int xx = x + dx[cur_d];
		if (yy < 1 || yy > n || xx < 1 || xx > n) break;
		if (mapp[yy][xx] == 1) break;
		if (mapp[yy][xx] != 9) {
			int ty = snake.front().first;
			int tx = snake.front().second;
			snake.pop();
			mapp[ty][tx] = 0;
		}
		snake.push(make_pair(yy, xx));
		mapp[yy][xx] = 1;
		cur_d = chdir(t);
	}
	return t;
}

int main() {
	cin >> n >> k;
	for (int i = 0; i < k;i++) {
		int y, x;
		cin >> y >> x;
		mapp[y][x] = 9;
	}
	cin >> L;
	for (int i = 0; i < L;i++) {
		int t;
		char d;
		cin >> t >> d;
		dir[t] = d;
	}
	cout << move();
}