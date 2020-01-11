#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int devideAndConquer(int arr[], int low, int high) {
    int i = low - 1;
    int pivot = arr[high];

    for(int idx = low; idx <= high; idx++) {
        if (arr[idx] < pivot) {
            ++i;
            swap(&arr[i], &arr[idx]);
        }
    }

    swap(&arr[i + 1], &arr[high]);

    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int i = devideAndConquer(arr, low, high);
        quickSort(arr, low, i - 1);
        quickSort(arr, i + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << ' ';
    }
}

int main() {
    int arr[10] = {10, 6, 2, 8, 5, 9, 1, 3, 7, 4};
    int N = 10;
    quickSort(arr, 0, N-1);
    printArray(arr, N);
}


