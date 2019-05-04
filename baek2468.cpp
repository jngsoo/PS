#include <iostream>
#include <string.h>
using namespace std;

int dy[4]={1,-1,0,0};
int dx[4]={0,0,1,-1};

int N;
int arr[100][100]={0};
int visited[100][100]={0};

void dfs(int y,int x,int height){
    
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        
        if(ny<0 || ny>=N || nx<0 || nx>=N)
            continue;
        
        if(arr[ny][nx]<=height || visited[ny][nx])
            continue;
        
        visited[ny][nx]++;
        dfs(ny,nx,height);
    }
    
}

int main(){
    
    cin>>N;
    
    int min_height=100,max_height=1;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&arr[i][j]);
            
            min_height=min(min_height,arr[i][j]);
            max_height=max(max_height,arr[i][j]);
        }
    }
    
    /*
     높이가 모두 1인 경우,
     0부터 물에 잠기지 않는 데 0값은 주어지지 않기 때문에 물에 잠기지 않는 경우의 수 없다
     
     if(max_height==1){
     cout<<0<<endl;
     return 0;
     }
     */
    
    
    int ans=1; //물에 잠기지 않는 영역의 최대 값
    for(int height=min_height;height<max_height;height++){
        
        memset(visited,0,sizeof(visited));
        
        int cnt=0; //물에 잠기지 않는 영역
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(arr[i][j]>height && !visited[i][j]){
                    visited[i][j]++;
                    cnt++;
                    dfs(i,j,height);
                }
            }
        }
        
        ans=max(ans,cnt);
    }
    
    cout<<ans<<endl;
    return 0;
}

