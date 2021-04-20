/*
14889. 스타트와 링크
210419 Solution
예전에 이 비슷한 문제 있었는데 링크 걸어놓기
1. dfs로 어차피 팀을 반으로 나누면 나머지 선택되지 않은 사람들이 한 팀이 되기 때문에 깊이 n/2까지 탐색
2. 탐색 가능한 범위는 내 뒤에 남은 사람들이 선택해야 될 사람 수보다 크거나 같을 경우에만 해당; 아니면 break
3. 팀이 결정되면 해당 팀에 대한 능력치 합의 차를 구해서 res와 비교
4. 백트래킹인 이유는 8명의 사람일 경우 8명을 전부 다 탐색할 필요가 없기 때문?
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

int n, res;
int selected[21] = {0,};
int stats[21][21] = {0,};

int calc(int sel1[], int sel2[]) {
	int sum1 = 0, sum2 = 0;
	for (int i = 0; i < n / 2; i++) {
		for (int j = i+1; j < n / 2; j++) {
			sum1 += stats[sel1[i]][sel1[j]] + stats[sel1[j]][sel1[i]];
			sum2 += stats[sel2[i]][sel2[j]] + stats[sel2[j]][sel2[i]];
		}
	}
	return abs(sum1 - sum2);
}

void dfs(int idx, int cnt) {
	if (cnt == n/2) {
		int sel1[10];
		int sel2[10];
		int idx1 = 0, idx2 = 0;
		for (int i = 1; i < n + 1; i++) {
			if (selected[i]) sel1[idx1++] = i;
			else sel2[idx2++] = i;
		}
		int ans = calc(sel1, sel2);
		if (res > ans) res = ans;
		return;
	}
	
	for (int i = idx; i < n+1; i++) {
		if (n + 1 - i >= n / 2 - cnt) {
			selected[i] = 1;
			dfs(i + 1, cnt + 1);
			selected[i] = 0;
		}
		else break;
	}

}

int main() {
    ios_base::sync_with_stdio(0);
	cin >> n;
	for (int i = 1; i < n+1; i++) {
		for (int j = 1; j < n+1; j++) {
			cin >> stats[i][j];
		}
	}
	res = 20 * 100;
	dfs(1, 0);
	cout << res;
}