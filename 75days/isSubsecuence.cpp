
#include <iostream>
#include <string>
#include <map>

using namespace std;

bool isSubsequence(string s, string t) {
    
    if (s == t) return true;
    int ptr = 0;
    char curr_target,curr;

    for (int i = 0; i < t.length(); i++) {

        curr_target = s[ptr];
        curr = t[i];

        if (curr == curr_target) {
            ptr++;
        }
        if (ptr == s.length()) {
            return true;
        }
    }

    if (ptr == s.length()) {
        return true;
    }
    return false;


}


int main() {


    cout << isSubsequence("axc", "ahbgdc");

    return 1;
}