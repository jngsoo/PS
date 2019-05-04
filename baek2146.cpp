#include <stdio.h>
#include <queue>
using namespace std;

#define LI    100000

int n;
int inputdata[100][100];
int map[100][100];
queue <pair<int, int>> que;
int dy[4] = { -1, 0, 0, 1 };
int dx[4] = { 0, -1, 1, 0 };

void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &inputdata[i][j]);
        }
    }
}


void dfs(int y, int x, int num) {
    int nexty, nextx;
    
    map[y][x] = num;
    
    for (int i = 0; i < 4; i++) {
        nexty = y + dy[i];
        nextx = x + dx[i];
        
        if (nexty >= 0 && nexty < n && nextx >= 0 && nextx < n) {           // 지도 좌표 범위 내인지 확인
            if (!map[nexty][nextx]) {                                             // not 방문이면
                if (inputdata[nexty][nextx])                                        // 섬이라면
                    dfs(nexty, nextx, num);                                          // dfs
                else {                                                                  // 섬이 아니면 (바다)
                    map[nexty][nextx] = num + 1;                                     // 방문
                    que.push(make_pair(nexty, nextx));                                // 섬이면 큐에 push
                }
            }
        }
    }
}

void island() {
    for (int i = 0, cnt = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (inputdata[i][j] && !map[i][j]) {                    // 섬인데 방문 안한 경우
                dfs(i, j, cnt * LI);                                  // dfs
                cnt++;
            }
        }
    }
}

int linkbridge() {
    int x, y;
    int nexty, nextx;
    int min = n * n;
    int temp;
    
    while (!que.empty()) {
        y = que.front().first;
        x = que.front().second;
        que.pop();
        
        for (int i = 0; i < 4; i++) {
            nexty = y + dy[i];
            nextx = x + dx[i];
            
            if (nexty < n && nexty >= 0 && nextx < n && nextx >= 0) {
                if (map[nexty][nextx]) {                                                    //바다가 아닌 경우
                    if (map[nexty][nextx] / LI != map[y][x] / LI) {                     // 단지가 같지 않을 경우
                        temp = map[nexty][nextx] % LI + map[y][x] % LI;
                        
                        if (temp < min)    min = temp;                                  // 육지 안쪽말고 가장 바깥쪽을 min으로
                    }
                }
                else {                                                                      //바다인 경우
                    map[nexty][nextx] = map[y][x] + 1;                                  // 가장자리에서 바다에서 떨어진 만큼
                    que.push(make_pair(nexty, nextx));                                  // 바다에서 주변 탐색
                }
            }
        }
    }
    
    return min;
}


int main() {
    input();
    island();
    printf("%d\n", linkbridge());
    return 0;
    
}

/*
 inputdata
 10
 1 1 1 0 0 0 0 1 1 1
 1 1 1 1 0 0 0 0 1 1
 1 0 1 1 0 0 0 0 1 1
 0 0 1 1 1 0 0 0 0 1
 0 0 0 1 0 0 0 0 0 1
 0 0 0 0 0 0 0 0 0 1
 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 1 1 0 0 0 0
 0 0 0 0 1 1 1 0 0 0
 0 0 0 0 0 0 0 0 0 0
 
 map
 100000 100000 100000 100001 100002 200002 200001 200000 200000 200000
 100000 100000 100000 100000 100001 100002 200002 200001 200000 200000
 100000 100001 100000 100000 100001 100002 200002 200001 200000 200000
 100001 100001 100000 100000 100000 100001 100002 200002 200001 200000
 100002 100002 100001 100000 100001 100002 100003 200002 200001 200000
 100003 100003 100002 100001 100002 300002 200003 200002 200001 200000
 100004 100004 100003 100002 300001 300001 300002 200003 200002 200001
 300004 300003 300002 300001 300000 300000 300001 300002 200003 200002
 300004 300003 300002 300001 300000 300000 300000 300001 300002 200003
 300005 300004 300003 300002 300001 300001 300001 300002 300003 200004
 */




