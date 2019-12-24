#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

#define SIZE 8

using namespace std;
string kingPosition, stonePosition, dir;
int N, kingX, kingY, stoneX, stoneY, moveDir, kingNextX, kingNextY, stoneNextX, stoneNextY;
int dx[SIZE] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[SIZE] = {1, 1, 0, -1, -1, -1, 0, 1};

int main() {

    cin >> kingPosition >> stonePosition >> N;

    // kingPostion, stonePosition x, y로 계산
    kingX = kingPosition[0] - 'A';
    kingY = '8' - kingPosition[1];
    stoneX = stonePosition[0] - 'A';
    stoneY = '8' - stonePosition[1];

    for (int i = 0; i < N; i++) {

        cin >> dir;

        // switch 못씀 (정수 유형(char, short, int, long, long long, enum) 만 평가 가능)
        if (!dir.compare("T")) moveDir = 0;
        else if (!dir.compare("RT")) moveDir = 1;
        else if (!dir.compare("R")) moveDir = 2;
        else if (!dir.compare("RB")) moveDir = 3;
        else if (!dir.compare("B")) moveDir = 4;
        else if (!dir.compare("LB")) moveDir = 5;
        else if (!dir.compare("L")) moveDir = 6;
        else if (!dir.compare("LT")) moveDir = 7;

        kingNextX = kingX + dx[moveDir];
        kingNextY = stoneX + dy[moveDir];

        // 지도 밖으로 넘어가면 거름
        if (kingNextX < 0 || kingNextY < 0 || kingNextX >= SIZE || kingNextY >= SIZE) continue;


        // 킹이 움직일 곳에 스톤이 놓여있으면 스톤 옮겨야댐 (킹 움직이는 같은 방향으로)
        if (kingNextX == stoneX && kingNextY == stoneY) {
            stoneNextX = stoneX + dx[moveDir];
            stoneNextY = stoneY + dy[moveDir];

            // 스톤 지도 밖으로 넘어가면 거름
            if (stoneNextX < 0 || stoneNextY < 0 || stoneNextX >= SIZE || stoneNextY >= SIZE) continue;

            stoneX = stoneNextX;
            stoneY = stoneNextY;
        }
        kingX = kingNextX;
        kingY = kingNextY;
    }

    cout << (char)(kingX + 'A') << SIZE  - kingY << endl;
    cout << (char)(stoneX + 'A') << SIZE - stoneY;

    return 0;
}