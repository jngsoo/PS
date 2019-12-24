#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

void printArr(long long arr[], int length) {
    for(int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }
}

int main() {

    int N, C;
    long long x[200001];

    scanf("%d %d", &N, &C);         // Input
    for (int i = 0; i < N; i++){
        scanf("%lld", &x[i]);
    }

    sort(x, x+N);              // Sort (DESC)


    printArr(x, N);

    return 0;
}
