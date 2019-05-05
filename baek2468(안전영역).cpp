#include <iostream>
#include <string.h>
using namespace std;

/*
 
 5
 
 6 8 2 6 2
 3 2 3 4 6
 6 7 3 3 2
 7 2 5 3 6
 8 9 5 2 7
 
 */

//우 좌 하 상
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

int N;
int arr[100][100]={0};                   // map
int visited[100][100]={0};               // visitedmap (0 혹은 1 둘 중 하나값만 가짐)

void printVisited() {
    for (int i=0; i<5; i++) {
        for (int j=0; j<5; j++){
            printf("%d ",visited[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void dfs(int y,int x,int height){
    
    for(int i=0;i<4;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        
        if(nx<0 || nx>=N || ny<0 || ny>=N)              // 지도 범위 밖?
            continue;
        
        if(arr[ny][nx]<=height || visited[ny][nx])      // 물에 잠기거나 이미 방문한 경우
            continue;
        
        printVisited();
        printf("nx is %d | ny is %d\n",nx,ny);
        visited[ny][nx]++;
        
        dfs(ny,nx,height);
        
    }
}



int main(){
    
    cin>>N;
    
    int min_height=100,max_height=1;
    
    // input 받고 min_height, max_height 설정 (2,9)
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&arr[i][j]);
            
            min_height=min(min_height,arr[i][j]);
            max_height=max(max_height,arr[i][j]);
        }
    }
    
    int ans=1;                                                      // 물에 잠기지 않는 영역의 최댓값 1로 초기화
    for(int height = min_height; height < max_height; height++){    // 강수량을 min_height 부터 max_height-1 까지 1씩 늘려가며
        
        //        printf("\nwhen height is %d\n",height);
        memset(visited,0,sizeof(visited));
        
        int cnt=0; //물에 잠기지 않는 영역
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(arr[i][j]>height && !visited[i][j]){     // 물에 잠기지 않고 아직 방문 안한 경우
                    visited[i][j]++;                        // 방문(1)
                    cnt++;
                    dfs(i,j,height);
                }
            }
        }
        //        printf("when height is %d, cnt is %d\n",height,cnt);
        ans=max(ans,cnt);
    }
    
    cout<<ans<<endl;
    return 0;
}


/*
 inputdata
 
 5
 6 8 2 6 2
 3 2 3 4 6
 6 7 3 3 2
 7 2 5 3 6
 8 9 5 2 7
 
 */
