// baek1890 점프
#include <iostream>

using namespace std;


int a;
int gamepan[101][101];

void input() {
    cin >> a;
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++){
            scanf("%d", &gamepan[i][j]);
        }
    }
}

void print_gamepan() {
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++){
            printf("%d ",gamepan[i][j]);
        }
        printf("\n");
    }
}

void print_as_input() {
    char input[101];
    while (fgets(input, 101, stdin))
        printf("%s",input);
}

int main() {
    
    //    input();
    //    print_gamepan();
    
    print_as_input();
    return 0;
}
