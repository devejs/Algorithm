/*
21609. 상어 중학교
210510 Solution
1. 가장 큰 그룹의 블록 수가 1이 될때까지 solve 루프 반복
2. 맵을 돌면서 자연수 블록일 때를 시작점으로 해서 덩어리 찾기(같은 수, 0)
3. 덩어리를 찾을 때 주의할 점!! 무지개 블록(0)은 다른 블록에서도 사용될 수 있으므로 덩어리가 끝나면 visited 초기화해주기
4. 블록 수, 블록 수가 같으면 무지개 블록 수에 따라 최대일 때의 좌표 저장
5. 4에서 좌표를 저장할 때 블록 수와 무지개 블록 수가 전부 같으면 행과 열이 가장 큰 마지막 원소가 해당된다.
6. 벡터에서 가장 마지막 원소를 빼내 해당 덩어리의 값을 초기화하고, 스코어를 더해준다.
7. gravity(), rotate(), gravity() 순서로 arr 맵을 정리해준다.
*/
#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
using namespace std;

int n, m;
int arr[20][20] = {0,};
int dx[4] = {0,1,0,-1};
int dy[4] = {-1,0,1,0};
int score = 0;
int maxx = 0, rainbow = 0;
vector<pair<int,int> > group;
bool visited[20][20] = {false,};

void rotate(){
    int temp[20][20] = {0,};
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            temp[n-j-1][i] = arr[i][j];
        }
    }
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            arr[i][j] = temp[i][j];
        }
    }
}

void find_group(int row, int col){
    int cnt = 1;
    int zero_cnt = 0;
    queue<pair<int,int> > q;
    q.push(make_pair(row,col));
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int i=0; i<4; i++){
            int yy = y+dy[i];
            int xx = x+dx[i];
            if (yy < 0 || yy >= n || xx < 0 || xx >= n || visited[yy][xx]) continue;
            if (arr[yy][xx] == arr[row][col] || arr[yy][xx] == 0){
                if (arr[yy][xx] == 0) zero_cnt++;
                cnt++;
                visited[yy][xx] = true;
                q.push(make_pair(yy,xx));
            }
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(visited[i][j] && !arr[i][j]) visited[i][j] = false;
        }
    }
    if (cnt > maxx || (cnt == maxx && zero_cnt > rainbow)){
        maxx = cnt;
        rainbow = zero_cnt;
        group.clear();
        group.push_back(make_pair(row, col));
    }else if (cnt == maxx && zero_cnt == rainbow){
        group.push_back(make_pair(row, col));
    }
}

void get_score(){
    int y = group.back().first;
    int x = group.back().second;
    int ch_val = arr[y][x];
    bool check[20][20] = {false,};
    check[y][x] = true;
    arr[y][x]= 6;
    queue<pair<int,int> > q;
    q.push(make_pair(y,x));
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int i=0; i<4; i++){
            int yy = y+dy[i];
            int xx = x+dx[i];
            if (yy < 0 || yy >= n || xx < 0 || xx >= n || check[yy][xx]) continue;
            if (arr[yy][xx] == ch_val || arr[yy][xx] == 0){
                arr[yy][xx] = 6;
                check[yy][xx] = true;
                q.push(make_pair(yy,xx));
            }
        }
    }
    score += maxx*maxx;
}

void gravity(){
    for (int j=0; j<n; j++){
        int blank = 0;
        for(int i=n-1; i>=0; i--){
            if (arr[i][j] == 6) blank++;
            else if (arr[i][j] == -1) blank = 0;
            else{
                if (blank == 0) continue;
                arr[i+blank][j] = arr[i][j];
                arr[i][j] = 6;
            }
        }
    }
}

int solve(){
    while (1){
        memset(visited, false, sizeof(visited));
        group.clear();
        maxx = 0;
        rainbow = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (!visited[i][j] && arr[i][j] > 0 && arr[i][j] < 6){
                    visited[i][j] = true;
                    find_group(i,j);
                }
            }
        }
        if (maxx < 2) break;
        get_score();
        gravity();
        rotate();
        gravity();
    }
    return score;
}

int main() {
    cin >> n >> m;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cin >> arr[i][j];
        }
    }
    cout << solve();
}