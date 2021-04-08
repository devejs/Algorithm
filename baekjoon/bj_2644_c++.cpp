/*
2644. 촌수 계산
210407 Solution
1. 자식이 몇 명 있는지 알 수 없으므로 vector 사용
2. bfs로 부모/자식(1촌) 탐색
3. 시작 노드에서부터 시작해서 도착 노드일 때의 거리(dist) 리턴
4. 거리값은 큐에 넣어서 저장하는 대신에 거리 배열을 만들어 시작점으로부터의 거리를 각 인덱스에 저장
*/

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int num;
int a, b;
vector<int> arr[101];

int bfs(int start, int dest) {
	int dist[101] = {0, };
	queue<int> q;
	q.push(start);
	while (!q.empty()) {
		int node = q.front();
		q.pop();
		if (node == dest) {
			return dist[dest]; 
		}
		int size = arr[node].size();
		for (int i = 0; i < size; i++) {
			int next = arr[node][i];

			if (!dist[next]) {
				q.push(next);
				dist[next] = dist[node] + 1; 
			}
		}
	}
	return -1;
}

int main() {
	int a, b, m;
	cin >> num >> a >> b >> m;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		arr[x].push_back(y);
		arr[y].push_back(x);
	}
	cout << bfs(a, b);
	return 0;
}

/*
페어 사용했을 때 메모리 초과난 거 다시 풀어보기
*/