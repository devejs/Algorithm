/*
4485. 녹색 옷 입은 애가 젤다지?
210506 Solution
1. bfs이되 중복 처리 안하는 bfs로 풀이
2. 중복처리 해주게 될 경우 이미 지나친 점에 대해서 최솟값 업데이트가 안 됨
*/

#include <iostream>
#include <algorithm>
#include <string.h>
#include <queue>
using namespace std;

int n;
int mapp[125][125];
int money[125][125];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };

int bfs() {
	queue<pair<int, int> > q;
	money[0][0] = mapp[0][0];
	q.push(make_pair(0, 0));
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int yy = y + dy[i];
			int xx = x + dx[i];
			if (yy < 0 || yy >= n || xx < 0 || xx >= n) continue;
			if (money[y][x] + mapp[yy][xx] < money[yy][xx] || money[yy][xx] == -1) {
				money[yy][xx] = money[y][x] + mapp[yy][xx];
				q.push(make_pair(yy, xx));
			}
		}
	}
	return money[n - 1][n - 1];
}

int main() {
	int tc = 1;
	int res = 0;
	while (1) {
		cin >> n;
		if (n == 0) break;
		memset(mapp, 0, sizeof(mapp));
		memset(money, -1, sizeof(money));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> mapp[i][j];
			}
		}
		res = bfs();
		cout << "Problem " << tc++ << ": " << res << '\n';
	}
	return 0;
}

/*
우선 순위 큐 사용 안하고 그냥 bfs로 풀이
메모리 사이즈가 작아서 가능했지 아니었으면 백퍼 시간 초과 났을 듯
우선 순위 큐로도 풀어보기
*/