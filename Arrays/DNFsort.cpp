#include <bits/stdc++.h>
using namespace std;

void PerformDNFSort(vector<int> &arr)
{
    int n = arr.size();
    int low, mid, high; // low = 0, mid = 1, high = 2;
    low = 0, mid = 0;
    high = n - 1;

    while (mid <= high)
    {
        switch (arr[mid])
        {
        case 0:
            swap(arr[low], arr[mid]);
            low++;
            mid++;
            break;
        case 1:
            mid++;
            break;
        case 2:
            swap(arr[mid], arr[high]);
            high--;
            break;
        }
    }
}

void PrintArray(vector<int> arr)
{
    for (auto it : arr)
    {
        cout << it << " ";
    }
    cout << "\n";
}

int main()
{
    vector<int> arr = {0, 1, 2, 0, 1, 2, 0, 1, 2};
    PrintArray(arr);
    PerformDNFSort(arr);
    PrintArray(arr);
    return 0;
}