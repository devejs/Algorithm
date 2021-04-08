/*
6603. 로또
210407 Solution
1. dfs로 개수가 6개 될 때 해당 수열 출력
2. 이미 정렬된 수이므로 앞에서부터 순서대로 선택하되 break 조건
3. break 조건 k-i == 6-d; 
    인덱스(i)가 하나씩 증가하므로 총 개수(k)-i 가 6-현재 고른 개수(d) 와 같으면 그 다음 인덱스에서는 개수가 부족하다
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int k;
vector<int> set;

void print(int* arr) {
	for (int i = 0; i < 6; i++) {
		cout << arr[i] << ' ';
	}
	cout << '\n';
}

void dfs(int idx, int d, int* arr) {
	if (d == 6) print(arr);
	for (int i = idx; i < k; i++) {
		arr[d] = set[i];
		dfs(i + 1, d + 1, arr);
		if (k - i == 6 - d) break;
	}
}

int main() {
	while (1) {
		cin >> k;
		if (k == 0) break;
		set.clear();
		for (int i = 0; i < k; i++) {
			int temp;
			cin >> temp;
			set.push_back(temp);
		}
		int arr[6] = { 0, };
		dfs(0, 0, arr);
		cout << '\n';
	}
	return 0;
}