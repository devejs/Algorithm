/*
1912. 연속합
210503 Solution
1. 정해지지 않은 개수의 연속된 수의 합이므로 항상 바로 앞의 수를 포함하는지 아닌지를 비교한다.
2. dp 배열에는 어떤 위치의 수가 맨 앞에서부터 더해져왔을 때의 최댓값을 저장한다.
3. 즉, i번째 수에는 i-1번째의 dp값이 최댓값이므로 이 값이 0보다 크면 더하고, 0보다 작으면 더하지 않는다.
*/

#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[100000] = { 0, };
int dp[100000] = { 0, };
int res;

int main() {
	cin >> n;
	for (int i = 0;i < n; i++) {
		cin >> arr[i];
	}
	dp[0] = arr[0];
	res = dp[0];
	for (int i = 1; i < n; i++) {
		dp[i] = max(dp[i - 1], 0) + arr[i];
		if (dp[i] > res) res = dp[i];
	}
	cout << res;
}