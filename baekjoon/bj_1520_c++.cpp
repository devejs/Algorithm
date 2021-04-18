/*
1520. 내리막 길
210418 Solution
dfs나 bfs로 풀면 시간초과
1. bfs+dp로 어떤 점에서 목적지에 도착할 수 있는 경로의 수를 저장
2. 방문하지 않았다는 의미로 dp 배열 -1로 초기화
2-1. 0으로 초기화할 경우 방문을 했지만 목적지에 도달할 수 없는 점인지 방문을 안 한 점인지 구별할 수 없음
3. dfs로 목적지에 도착하면 1 리턴
4. dfs 탐색시 dp 값이 -1이 아니면 이미 방문한 곳이므로 dp값 리턴
5. 내리막길일 때만 현재 dp값에 bfs 리턴값 더해줌
*/

#include <iostream>
#include <cstring>

using namespace std;

int m, n;
int mapp[501][501] = { 0, };
int dp[501][501] = { 0, };
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,-1,0,1 };

int dfs(int y, int x) {
	if (y == m - 1 && x == n - 1) return 1;
	if (dp[y][x] != -1) return dp[y][x];

	dp[y][x] = 0;
	for (int i = 0; i < 4; i++) {
		int yy = y + dy[i];
		int xx = x + dx[i];
		if (yy < 0 || yy >= m || xx < 0 || xx >= n) continue;
		if (mapp[yy][xx] < mapp[y][x]) {
			dp[y][x] += dfs(yy, xx); 
		}
	}
	return dp[y][x];
}

int main() {
	cin >> m >> n;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cin >> mapp[i][j];
		}
	}
	memset(dp, -1, sizeof(dp));
	cout << dfs(0, 0);
}