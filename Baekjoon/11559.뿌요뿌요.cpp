#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

int toBeBoomOrNot = 0;

char map[12][6];
bool visited[12][6];
int nx, ny;

bool flag;  // 뿌요 한묶음 터지면 true 로 할거임
int answer = 0;

vector<pair<int, int>> sameColorBooms, allTheBooms;

void printMap() {
    cout << endl;
    for (int y = 0; y < 12; y++){
        for (int x = 0; x < 6; x++) {
            cout << map[y][x];
        }
        cout << endl;
    }
    cout << endl;
}


void DFS(int x, int y) {
    for (int i = 0; i < 4; i++){
        nx = x + dx[i];
        ny = y + dy[i];

        if (nx < 0 || nx >= 6 || ny < 0 || ny >= 12) continue; // 지도 범위 확인
        if (map[ny][nx] == '.') continue; // 뿌요 아닌곳 거름
        if (visited[ny][nx]) continue; // 이미 방문한 곳 거름
        if (map[y][x] != map[ny][nx]) continue; // 같은 색 뿌요 아니면 거름

        toBeBoomOrNot++;            // 같은 색 뿌요 갯수 증가 (4개 이상인지 나중에 확인)
        sameColorBooms.push_back(make_pair(nx,ny));     // 나중에 터뜨릴(4개 이상일 때) 뿌요들의 좌표 저장
        visited[ny][nx] = true;           // 방문 표시

        DFS(nx, ny);
    }
}

int main() {

    // INPUT
    for(int row = 0; row < 12; row++){
        for(int col = 0; col < 6; col++){
            cin >> map[row][col];
        }
    }

    while(true) {
        flag = false;
        memset(visited, false, sizeof(visited));
        allTheBooms.clear(); // 같은 색 뿌요 저장하는 벡터 초기

        // 지도 탐색
        for(int y = 0; y < 12; y++) {
            for(int x = 0; x < 6; x++) {
                if(map[y][x] != '.' && !visited[y][x]) {

                    toBeBoomOrNot = 1;  // 같은 색 뿌요 1로 시작
                    sameColorBooms.push_back(make_pair(x,y));
                    visited[y][x] = true;
                    DFS(x,y);

                    if (toBeBoomOrNot >= 4) {
                        flag = true;
                        int size = sameColorBooms.size();
                        for (int i = 0; i < size; i++){
                            allTheBooms.push_back(sameColorBooms[i]);
                        }
                    }
                    sameColorBooms.clear();
                }
            }
        }

        // 뿌요 터뜨리기
        int size = allTheBooms.size();
        for(int i = 0; i < size; i++){
            int boomX = allTheBooms[i].first;
            int boomY = allTheBooms[i].second;

            map[boomY][boomX] = '.';
        }


        // 지도 정리 (뿌요들 내려주기)
        for (int i = 10; i >= 0; i--) {
            for (int j = 0; j < 6; j++) {
                if (map[i][j] == '.') continue;
                int temp = i;

                while (true) {
                    if (temp == 11 || map[temp + 1][j] != '.') break;

                    map[temp + 1][j] = map[temp][j];
                    map[temp][j] = '.';
                    temp++;
                }
            }
        }

        if(flag) answer++;
        else break;
    }

    cout << answer;
    return 0;
}