#include<iostream>
#include<bits/stdc++.h>
using namespace std;



bool isIsomorphic(string s, string t) {
    map<char,char> map1,map2;
    int ptr1 =0,ptr2 =0;
    char val1,val2;
    while (ptr1 < map1.size()){

        val1 = s[ptr1];
        val2 = s[ptr2];
            
        if(!map1[val1] && !map2[val2]){
            map1[val1] = val2;
            map2[val2] = val1;
            
        }else if(map1[val1] != val2 || map2[val2] != val1){
            return false;
        }
        ptr1++;
        ptr2++;
    }
     return true;
}


int main(){
    cout<<isIsomorphic("foo", "bar");
    return 0;
}
