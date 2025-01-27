// Reverse the Array

#include <bits/stdc++.h>
using namespace std;

void ReverseArray(vector<int> &arr)
{
    int len = arr.size();
    if (len <= 0)
    {
        cout << "Revese Not Possible \n";
        return;
    }
    int i = 0;
    int j = len - 1;
    while (i <= j)
    {
        swap(arr[i], arr[j]);
        i++;
        j--;
    }
}

void PrintArray(vector<int> arr)
{
    for (auto it : arr)
    {
        cout << it << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> arr = {6, 5, 4, 3, 2, 1};
    // Display Array before Reversing :
    PrintArray(arr);
    // Reverse Array
    ReverseArray(arr);
    // Display Array after Reversing :
    PrintArray(arr);
    return 0;
}