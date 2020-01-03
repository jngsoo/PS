#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, arr[1000000];

void getInput()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

void printArray()
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << endl;
    }
}

int main()
{
    getInput();
    printArray();
}