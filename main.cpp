#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool standard(const string &str1, const string &str2) {

    if (str1.size() == str2.size())      // 같은 길이의 단어들은 사전 순
        return str1 < str2;
    return str1.size() < str2.size();   // 다른 길이의 단어들은 길이 순
}


int main() {

    string word;
    int N;
    cin >> N;

    vector<string> vec;

    for (int i=0; i<N; i++) {
        cin >> word;
        vec.push_back(word);
    }

    sort(vec.begin(), vec.end(), standard);     // standard 기준으로 Vector 정렬

    cout << vec[0] << endl;
    for(int i=1; i<N; i++) {                    // 같은 단어(중복 여부) 검사
        if (vec[i]!=vec[i-1])
            cout << vec[i] << endl;
    }

    return 0;
}




