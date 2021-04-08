/*
2529. 부등호
210407 Solution
1. 부등호의 최대 개수로 부등호 배열, 숫자 배열, 사용한 배열(방문 처리) 만들기
2. 완전 탐색으로 모든 수를 다 시도해보기 위해 맨 첫번째 인덱스에 포문으로 값 넣기
3. 부등호를 비교해가면서 불가하면 break, 되면 dfs 탐색
4. 현재 위치(숫자 위치)가 부등호의 개수와 동일해지면 현재 값(문자열) 최대, 최소와 각각 비교
*/
#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

int num;
bool used[10] = { false, };
char sign[10] = { '\0', };
char acc[11];
char res[2][11] = { "999999999","0" };

void search(int loc, char n) {
	if (loc == num) {
		if (strcmp(acc, res[0]) < 0) strcpy(res[0], acc);
		if (strcmp(acc, res[1]) > 0) strcpy(res[1], acc);
		return;
	}
	if (sign[loc] == '<') {
		// 오른쪽이 더 큼
		for (char r = '9'; r > n; r--) {
			int idx = r - '0';
			if (!used[idx]) {
				used[idx] = true;
				acc[loc + 1] = r;
				search(loc + 1, r);
				used[idx] = false;
				acc[loc + 1] = '\0';
			}
		}
	}
	else {
		// 왼쪽이 더 큼
		for (char i = '0'; i < n; i++) {
			int idx = i - '0';
			if (!used[idx]) {
				used[idx] = true;
				acc[loc + 1] = i;
				search(loc + 1, i);
				used[idx] = false;
				acc[loc + 1] = '\0';
			}
		}
	}
}

int main() {
	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> sign[i];
	}
	for (char c = '0'; c <='9'; c++) {
		memset(used, false, sizeof(used));
		memset(acc, '\0', sizeof(acc));
		acc[0] = c;
		used[c - '0'] = true;
		search(0, c);
		//print();
	}
	cout << res[1] << '\n';
	cout << res[0] << '\n';
	return 0;
}


/*
문자열 처리하는데 생고생함.. 나중에 까먹을 때쯤 한번 더 풀어보기
*/