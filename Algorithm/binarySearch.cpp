#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

void printArr(int arr[], int length) {
    for(int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}


int main() {
//    binary search
    int N, target, startIdx, midIdx, endIdx, midValue;
    int arr[10001];

    scanf("%d %d", &N, &target);
    for(int i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }

    sort(arr, arr+N);
    printArr(arr, N);

    startIdx = 0;
    endIdx = N-1;

    while (startIdx <= endIdx) {
        midIdx = (startIdx + endIdx) / 2;

        printf("%d %d %d\n", arr[startIdx], arr[midIdx], arr[endIdx]);
        midValue = arr[midIdx];

        if (midValue == target) {
            printf("%d", midValue);
            return midValue;
        }

        if (midValue > target) {
            endIdx = midIdx - 1;
        }

        else {
            startIdx = midIdx + 1;
        }
    }
    printf("x");
    return 'x';

}

/* Test case
 *
    10 7
    1 3 5 7 9 11 13 15 17 20

    10 10
    1 3 5 7 9 11 13 15 17 20
 *
 * */
