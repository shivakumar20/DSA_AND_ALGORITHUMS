#include <bits/stdc++.h>
using namespace std;

void PrintKthMinMaxEle(vector<int> &arr, int pos)
{
    // ToDo : Come up with an algorithm
    // Brute Force: Sort the array and then move K positions to front and back.
    int len = arr.size() - 1;
    // sort(arr.begin(), arr.end());
    // cout << arr[len - pos] << endl;
    // cout << arr[pos] << endl;

    // Brute Better : Priority Queue

    priority_queue<int> pq;
    priority_queue<int, vector<int>, greater<int>> spq;
    for (int i = 0; i < arr.size(); i++)
    {
        pq.push(arr[i]);
        spq.push(arr[i]);
    }

    int find = pos - 1;
    while (find > 0)
    {
        pq.pop();
        spq.pop();
        find--;
    }

    cout << pq.top() << "\t" << spq.top() << endl;
}

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    int k;
    cin >> k;
    PrintKthMinMaxEle(arr, k);
    return 0;
}