/*
1149. RGB 거리
210428 Solution
이전에 파이썬으로 풀어본 문제임
https://github.com/coding-mates/Algorithm_v2/blob/main/Eunjee/Baekjoon%201149%20Python.py
1. 현재(n) 집을 색칠 할 수 있는 가짓수는 3가지(RGB)
2. 현재 집을 색칠하기 위해서 이전 집의 색깔 가짓수는 2가지
3. 2번에서 가능한 2가지의 누적 비용을 비교하여 더 작은 값과 더해서 저장한다.
4. 단, 1번에서 말했듯이 가능한 가짓수가 3가지이므로 각각의 경우의 수를 계산한 3의 값을 전부 저장한다.
*/
#include <iostream>
#include <algorithm>
using namespace std;

int n;
int cost[1001][3] = { 0, };

int main() {
	cin >> n;
	for (int i = 1; i < n + 1; i++) {
		cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
	}

	for (int i = 2; i < n + 1; i++) {
			for (int j = 0; j < 3; j++)
				cost[i][j] += min(cost[i - 1][(j + 1) % 3], cost[i - 1][(j + 2) % 3]);
	}
	cout << min(min(cost[n][0], cost[n][1]), cost[n][2]);
}