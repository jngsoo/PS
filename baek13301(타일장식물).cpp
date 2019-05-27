#include <iostream>
#include <string>

using namespace std;

long long solution(int N) {
    long long t1 = 1;
    long long t2 = 1;
    long long sum;
    
    if (N==1)
        return 4;
    else{
        for(long long i = 2; i < N; i++){
            sum = t1 + t2;
            t1 = t2;
            t2 = sum;
        }
    }
    return ((t1+t2)+t2)*2;
}


int main() {
    int N;
    cin >> N;
    cout << solution(N) << endl;
    return 0;
}




