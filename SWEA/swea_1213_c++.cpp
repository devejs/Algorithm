/*
1213. String
210127 Solution
1. 문자열 길이 구하는 함수 직접 구현
2. 문장을 돌면서 찾으려는 문자열 하나씩 찾기
*/

#include <iostream>
using namespace std;

int get_length(char *str){
    int count = 0, i=0;

    while (str[i] != '\0'){
        count++;
        i++;
    }
    return count;
}

int main() {
    int tc_num, count;
    char find[11];
    char sentence[1001];

    for(int test_case = 1; test_case <= 10; ++test_case){
        cin >> tc_num;
        cin >> find;
        cin >> sentence;
        count = 0;

        for (int i=0; i < get_length(sentence); i++) {
            if (sentence[i] == find[0]) {
                int origin_i = i;
                int find_i = 1;
                for (int j = i+1 ; j < i+get_length(find); j++) {
                    if (sentence[j] != find[find_i] )  break;
                    if (j == i-1 + get_length(find)){
                        count++;
                        i = j;
                        if (j >= get_length(sentence)-1) {
                            cout << "#" << tc_num << " " << count << endl;
                            return 0;
                        }
                    }
                    find_i++;
                }
            }
        }
    cout << "#" << tc_num << " " << count << endl;
    }
    return 0;
}
