/*
2156. 포도주 꿍
210414 Solution
1. 3일 연속 포도주를 마실 수 없으므로 오늘 마실 때 지난 3일간 가능한 경우의 수는
--------------------------------------------------------
n-3 n-2 n-1 n
 O   X   X  O
     O   X  O
 O   X   O  O
--------------------------------------------------------
위 경우의 수에서 최종적으로 도출된 점화식은
d1 = dp[n-2]+podo[n]
d2 = dp[n-3]+podo[n-1]+podo[n]
2. 오늘 마시지 않을 경우, 이틀 연속으로 마시지 않을 수 있으므로 1번에서 더 큰 값과 dp[n-1], dp[n-2]를 비교하여 가장 큰 값을 저장한다.
3. 포도주의 수와 최댓값은 관계 없을 수 있으므로 매번 dp가 저장될 때마다 최댓값을 갱신해준다.
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int num;
vector<int> podo;
vector<int> dp;

int main() {
	int res = 0;
	cin >> num;
	for (int i = 0; i < num; i++) {
		int temp;
		cin >> temp;
		podo.push_back(temp);
	}
	for (int i = 0; i < num; i++) {
		if (i == 0) dp.push_back(podo[0]);
		else if (i == 1) dp.push_back(podo[0] + podo[1]);
		else if (i == 2) {
			int d1 = max(podo[0], podo[1]) + podo[2];
			dp.push_back(max(d1, dp[1]));
		}
		else {
			int d1 = max(dp[i - 2], dp[i - 3] + podo[i - 1]) + podo[i];
			dp.push_back(max(max(dp[i-2],dp[i-1]),d1));
		}
        if (dp[i] > res) res = dp[i];
	}
	cout << res;
	return 0;
}