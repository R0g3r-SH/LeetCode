#include <bits/stdc++.h>



using namespace std;

int longestPal (string s){

    map<char,int> map1;

    int maxlen;
    bool even = false;

    for(char charac : s){
        if (!map1[charac]){
            map1[charac]  =1;
         }
         else {
            map1[charac] ++;
         }
    }


    for (auto keys : map1){
        auto x = keys.second;

        //is odd number

        if (x%2 == 0){
            maxlen+= x;

        }else{
            even = true;
        }

    }   

    if (even) return  maxlen + 1;

    return maxlen;

}

int main (){
    string s = "abccccdd";
    cout << longestPal(s);
    return 0;
}





