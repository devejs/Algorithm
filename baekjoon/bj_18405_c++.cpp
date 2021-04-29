/*
18405. 경쟁적 전염
210429 Solution
1. 바이러스의 위치를 각 바이러스의 종류 배열 안의 벡터에 담는다
2. 바이러스의 위치와 시간값을 구조체에 담아 벡터 큐에 바이러스 종류가 작은 순서대로 넣는다(정렬)
3. bfs를 돌면서 상하좌우로 전염 가능한 구간을 전염시키고 큐에 넣는다. 
4. 3에서 1초가 지난 셈이므로 시간값을 증가시킨다.
5. 벡터 큐에 바이러스 종류가 정렬되어있으므로 추가된 구간도 정렬되어 큐에 들어가게 된다.
6. 주어진 시간을 만족하거나 구하려는 위치 값에 바이러스가 있으면 그 떄의 맵 값을 리턴한다. (이미 감염된 구간은 변하지 않으므로)
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, k;
int S, Y, X;
int mapp[201][201];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
struct Virus {
	int sec;
	int y, x;
	Virus(int s, int i, int j) : sec(s), y(i), x(j) {}
};
vector<Virus> q;

int bfs() {
	while (!q.empty()) {
		Virus v = q.front();
		if (v.sec == S || mapp[Y][X] != 0) break;
		q.erase(q.begin());
		for (int i = 0; i < 4; i++) {
			int yy = v.y + dy[i];
			int xx = v.x + dx[i];
			if (xx < 1 || xx > n || yy < 1 || yy > n || mapp[yy][xx] != 0) continue;
			mapp[yy][xx] = mapp[v.y][v.x];
			q.push_back(Virus(v.sec + 1, yy, xx));
		}
	}
	return mapp[Y][X];
}

int main() {
	vector<pair<int, int> > type[1001];
	cin >> n >> k;
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < n + 1; j++) {
			cin >> mapp[i][j];
			type[mapp[i][j]].push_back(make_pair(i, j));
		}
	}
	cin >> S >> Y >> X;
	for (int i = 1; i < 1001; i++) {
		for (int j = 0; j < type[i].size(); j++) {
			q.push_back(Virus(0, type[i][j].first, type[i][j].second));
		}
	}
	cout << bfs();
	return 0;
}

/*
문제 푸는거 자체는 오래 걸리지 않았는데 파이썬처럼 리스트에 제한이 없는 걸 잊음+문제 착각으로 큰 삽질
*/