include<stdio.h>

int max(int a, int b){return a > b? a : b;};
int main() {
    
    int n;  // 포도주 잔의 갯수
    int wines[10000];
    scanf("%d",&n);
    int accumWines[10000];
    
    for (int i=1; i<=n; i++) {
        int wine;
        scanf("%d",&wine);
        wines[i] = wine;
    }
    
    accumWines[0] = 0;
    accumWines[1] = wines[1];
    accumWines[2] = accumWines[1] + wines[2];
    
    for(int i = 3; i <= n; i++){
        int a = accumWines[i-1];
        int b = accumWines[i-2] + wines[i];
        int c = accumWines[i-3] + wines[i-1] + wines[i];
        accumWines[i] = max(a, max(b,c));
    }
    printf("%d", accumWines[n]);
    
    return 0;
    
}
