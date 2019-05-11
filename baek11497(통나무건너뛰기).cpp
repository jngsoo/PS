// baek11497 통나무 건너뛰기
#include <iostream>
#include <algorithm> //for sort
using namespace std;

int main(void) {
    
    int T,N,max,temp;
    int tong[10001];
    int restong[10001];
    
    cin >> T;
    for (int test_case = 0; test_case < T; test_case++) {
        
        cin >> N;
        for (int i=0; i<N; i++) {
            cin >> tong[i];
        }
        sort(tong,tong+N);                  // tong 정렬 (오름차순)
        
        //tong = {2,4,5,7,9}
        //restong should be {2,5,9,7,4}
        for (int i=0; i<N; i++) {           // 홀수 index는 앞에서부터, 짝수 index는 뒤에서부터 채움
            if (i%2==0)
                restong[(i+1)/2] = tong[i];
            else
                restong[N-1-(i/2)] = tong[i];
        }
        
        max = abs(restong[0]-restong[N-1]);     // 맨 앞 통나무와 맨 끝 통나무간 거리 차를 처음 max로 설정
        for (int i=0; i<N-1; i++) {
            temp = abs(restong[i] - restong[i+1]);      // restong 순회, 각 통나무 앞 뒤 간 거리계산하며 max값 수정
            if (temp>max)
                max = temp;
        }
        cout << max << endl;
    }
    
    return 0;
}
