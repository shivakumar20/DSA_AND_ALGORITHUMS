#include <bits/stdc++.h>
using namespace std;

pair<int, int> ReturnMinMax(vector<int> arr)
{
    int minEle = INT_MAX, maxEle = INT_MIN;
    for (int i = 0; i < arr.size(); i++)
    {
        // minEle = min(arr[i], minEle);
        // maxEle = max(arr[i], maxEle);
        if (arr[i] <= minEle)
        {
            minEle = arr[i];
        }
        if (arr[i] > maxEle)
        {
            maxEle = arr[i];
        }
    }
    return {minEle, maxEle};
}

int main()
{
    vector<int> arr = {1, 3, 2, 3, 4, 5, 9};
    pair<int, int> minMAx = ReturnMinMax(arr);
    cout << minMAx.first << " " << minMAx.second << "\n";
    return 0;
}