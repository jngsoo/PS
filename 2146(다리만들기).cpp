//백준2146 다리만들기

#include <stdio.h>
#include <queue>
using namespace std;

#define LI    100000

int n;
int inputdata[100][100];
int map[100][100];
queue <pair<int, int> > que;

//하-좌-우-상
int dx[4] = { 0, -1, 1, 0 };
int dy[4] = { -1, 0, 0, 1 };


void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &inputdata[i][j]);
        }
    }
}


void dfs(int x, int y, int num) {
    int nextx, nexty;
    
    map[x][y] = num;
    
    for (int i = 0; i < 4; i++) {
        nextx = x + dx[i];
        nexty = y + dy[i];
        
        if (nextx >= 0 && nextx < n && nexty >= 0 && nexty < n) {           // next x,y 좌표가 지도 범위 내에 해당되나 확인
            if (!map[nextx][nexty]) {                                             // next x,y 가 not 방문이면
                if (inputdata[nextx][nexty])                                        // next x,y 가 육지라면
                    dfs(nextx, nexty, num);                                            // dfs(재귀)
                else {                                                              // next x,y 가 육지가 아니면 (바다)
                    map[nextx][nexty] = num + 1;                                       // 가장자리 바다는 1만큼 더해서 표시
                    que.push(make_pair(nextx, nexty));                                 // next x,y 를 큐에 push
                }
            }
        }
    }
}

//각 섬에 번지 번호를 붙이는 함수 (10000, 20000, 30000, ...)  (섬의 인접 바다는 10001,20001,30001 ...)
void island() {
    for (int i = 0, cnt = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (inputdata[i][j] && !map[i][j]) {                    // 육지인데 방문 안한 경우
                dfs(i, j, cnt * LI);                                  // dfs
                cnt++;
            }
        }
    }
}

int linkbridge() {
    
    int x, y;
    int nextx, nexty;
    int min = n * n;            // 처음 min 값은 지도 내 최대 거리로 초기화
    int temp;
    
    while (!que.empty()) {      // que에는 바다
        x = que.front().first;
        y = que.front().second;
        que.pop();
        
        for (int i = 0; i < 4; i++) {
            nextx = x + dx[i];
            nexty = y + dy[i];
            
            if (nextx >= 0 && nextx < n && nexty >= 0 && nexty < n) {              // next x,y 좌표가 지도 범위 내에 해당되나 확인
                
                if (map[nextx][nexty]) {                                               // next x,y 가 육지 or 육지인접바다인 경우
                    if (map[nextx][nexty] / LI != map[x][y] / LI) {                        // 현재 x,y 와 next x,y 가 같은 구역(같은섬? 섬? 바다?)이 아닐 경우
                        temp = map[nextx][nexty] % LI + map[x][y] % LI;                        // 육지에서 바다까지 거리(next x,y) + 육지에서 바다까지 거리(x,y)
                        
                        if (temp < min)    min = temp;
                    }
                }
                
                else {                                                                 // next x,y 의 map 값이 0인 경우 (육지에 인접하지도 않은 바다)
                    map[nextx][nexty] = map[x][y] + 1;                                     // next x,y map 값에 x,y에서 1만큼 값(거리) 늘려서 설정
                    que.push(make_pair(nextx, nexty));                                     // 큐에 next x,y(바다) 넣음
                }
            }
        }
    }
    
    return min;
}

void printMap() {
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            printf("%6d ",map[i][j]);
        }
        printf("\n");
    }
}


int main() {
    
    
    input();
    
    printf("Before island()\n");
    printMap();
    
    
    
    island();
    
    
    
    printf("After island()\n");
    printMap();
    
    
    
    printf("%d\n", linkbridge());
    printf("After linkbridge()\n");
    printMap();
    
    
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
