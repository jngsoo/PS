// 비트 연산. 풀이 참조

#include <iostream>
using namespace std;

int main() {
    const int MOD = 1000000007;
    long long A, X, answer = 1;
    cin >> A >> X;

    A %= MOD;

    while (X >= 1) {
        if (X & 1) {
            answer = ( answer * A ) % MOD;
        }
        X = X >> 1;
        A = ( A * A ) % MOD;
    }

    cout << answer << endl;

    return 0;
}