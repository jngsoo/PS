// 이진 탐색
// long long 아닌 int 로 하면 틀렷다고

#include <iostream>
using namespace std;

int main() {
    long long N, M, left, right, answer;
    long long max = 0;
    long long trees[1000001];
    long long treesSum, mid;

    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        cin >> trees[i];
        if (trees[i] > max) max = trees[i];
    }

    left = 0;
    right = max;
    answer = 0;

    while (left <= right) {
        mid = ( left + right ) / 2;
        treesSum = 0;
        for(long long i = 0; i < N; i++) {
            if (trees[i] > mid) {
                treesSum += trees[i] - mid;
            }
        }

        if (treesSum >= M) {    // 조건 충족, mid 키워야
            if(answer < mid) {  // mid 최대값 구해
                answer = mid;
            }
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    cout << answer << endl;
}
