// 이진 탐색?

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M, arrN[100001], m, printNum;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arrN[i];
    }
    sort(arrN, arrN+N);

    cin >> M;
    for (int i = 0; i < M; i++) {
        printNum = 0;
        cin >> m;
        for (int j = 0; j < N; j++) {
            if (m == arrN[j]) {
                printNum = 1;
                break;
            }
        }
        cout << printNum << endl;
    }
}