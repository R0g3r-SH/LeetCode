#include <bits/stdc++.h>

using namespace std;

bool peaker(vector<int> nums, int target)
{
    if (nums[target - 1]<nums[target]> nums[target + 1])
    {
        return true;
    }
        return false;
}

int findPeakElement(vector<int> nums)
{

    for (int i = 1; i < (nums.size()-1); i++)
    {
        if (peaker(nums, i) ==true)
            return i;
    }

    return -1;
}

int main(){
    cout<< findPeakElement({1,2,3,1});

    return 0;
}