
#include <bits/stdc++.h>
using namespace std;


struct ListNode {

    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

ListNode* head = NULL;  

void insert(int new_data) {
   struct ListNode* new_node;
   new_node->val = new_data;
   new_node->next = head;
   head = new_node;
}

void printLinkedList (ListNode* l1){

    while(l1 != NULL){
        cout << l1->val;
        l1 = l1->next;
    }

}



ListNode* mergeTwoLists(ListNode* l1 ,ListNode* l2)
{
    insert(3);


}

int main(){





    return 0;
}