/*
15683. 감시
210411 Solution
1. 인풋 위치를 mapp에 저장하면서 감시카메라일 경우(1~5) 벡터 자료구조에 저장
2. 인덱스 0부터 벡터 자료구조를 하나씩 좌표 탐색하되, cctv의 종류에 따라 탐색 방향을 다르게 하여 dfs 탐색
3. 탐색 방향은 dx,dy를 이용하여 방향을 정하되 각 cctv 종류에 따라 감시 가능한 위치는 같은 복사 배열(위치mapp)에 9로 할당 (paint 함수)
4. 인덱스가 벡터의 사이즈와 동일하면 모든 cctv가 전부 동작하므로 남은 0의 개수가 곧 사각지대의 수
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n, m;
int mapp[8][8];
int res = 64;
vector<pair<int, int> > cctv;
int dx[4] = {0, 1, 0, -1}; // 상 우 하 좌
int dy[4] = {-1, 0, 1, 0};

int count(int arr[][8]) {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == 0) cnt++;
		}
	}
	return cnt;
}

void paint(int y, int x, int dir, int arr[][8]) {
	int idx = 1;
	while (y + idx * dy[dir] >= 0 && y + idx * dy[dir] < n && x + idx * dx[dir] >= 0 && x + idx * dx[dir] < m) {
		if (arr[y + idx * dy[dir]][x + idx * dx[dir]] == 6) break;
		else if (arr[y + idx * dy[dir]][x + idx * dx[dir]] == 0) arr[y + idx * dy[dir]][x + idx * dx[dir]] = 9;
		idx++;
	}
}

void search(int idx, int arr[][8]) {
	if (idx == cctv.size()) {
		int temp = count(arr);
		if (temp < res) res = temp;
		return;
	}
	int i = cctv[idx].first;
	int j = cctv[idx].second;
	switch(mapp[i][j]){
	case 1:
		for (int k = 0;k < 4; k++) {
			int new_arr[8][8];
			copy(&arr[0][0], &arr[0][0] + 8 * 8, &new_arr[0][0]);
			paint(i,j,k, new_arr);
			search(idx + 1, new_arr);
		}
		break;
	case 2:
		for (int k = 0; k < 2; k++) {
			int new_arr[8][8];
			copy(&arr[0][0], &arr[0][0] + 8 * 8, &new_arr[0][0]);
			paint(i, j, k, new_arr);
			paint(i, j, k+2, new_arr);
			search(idx + 1, new_arr);
		}
		break;
	case 3:
		for (int k = 0; k < 4; k++) {
			int new_arr[8][8];
			copy(&arr[0][0], &arr[0][0] + 8 * 8, &new_arr[0][0]);
			paint(i, j, k, new_arr);
			paint(i, j, (k+1)%4, new_arr);
			search(idx + 1, new_arr);
		}
		break;
	case 4:
		for (int k = 0; k < 4; k++) {
			int new_arr[8][8];
			copy(&arr[0][0], &arr[0][0] + 8 * 8, &new_arr[0][0]);
			for (int p = 0; p < 4; p++) {
				if (k == p) continue;
				paint(i, j, p, new_arr);
			}
			search(idx + 1, new_arr);
		}
		break;
	case 5:
		int new_arr[8][8];
		copy(&arr[0][0], &arr[0][0] + 8 * 8, &new_arr[0][0]);
		for (int k = 0; k < 4; k++) paint(i, j, k, new_arr);
		search(idx + 1, new_arr);
		break;
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> mapp[i][j];
			if (mapp[i][j] >= 1 && mapp[i][j] < 6) {
				cctv.push_back(make_pair(i, j));
			}
		}
	}
	int arr[8][8];
	copy(&mapp[0][0], &mapp[0][0] + 8 * 8, &arr[0][0]);
	search(0, arr);

	cout << res;
	
	return 0;
}