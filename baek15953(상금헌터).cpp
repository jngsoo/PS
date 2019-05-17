#include <iostream>
using namespace std;

int prize_2017(int rank) {
    if (rank < 2)
        return 5000000;
    else if (rank < 4)
        return 3000000;
    else if (rank < 7)
        return 2000000;
    else if (rank < 11)
        return 500000;
    else if (rank < 16)
        return 300000;
    else if (rank < 22)
        return 100000;
    else
        return 0;
}

int prize_2018(int rank) {
    if (rank < 2)
        return 5120000;
    else if (rank < 4)
        return 2560000;
    else if (rank < 8)
        return 1280000;
    else if (rank < 16)
        return 640000;
    else if (rank < 32)
        return 320000;
    else
        return 0;
}

int main() {
    
    int T,rank_2017,rank_2018,total_prize;
    
    cin >> T;
    for (int i=0; i<T; i++){
//        scanf("%d %d", rank_2017, rank_2018);     왜 안됨?
        cin >> rank_2017 >> rank_2018;
        total_prize = prize_2017(rank_2017) + prize_2018(rank_2018);
        cout << total_prize << endl;
    }
    
    return 0;
}



