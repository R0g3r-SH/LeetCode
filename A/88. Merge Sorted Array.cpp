#include <iostream>
#include <bits/stdc++.h>



void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

    int p1 = m -1;
    int p2 = m - 2; 

    ///     |
    // [1,2,3,0,0,0]

    for (int p = nums.size()-1 ; p >=0 ; p --){

        if (p2<0){
            break;
        }

        if (p1>0 && nums1[p1] > nums[p2]){
            nums1[p] = nums1[p1--];
        }else{
            nums[p] = nums[p2--];
         }
    } 
        
}

int main(){
    return 0;
}