#include<bits/stdc++.h>
using namespace std;
struct HackNode
{
    char key;
    HackNode *left;
    HackNode *right;
    HackNode(char val)
    {
        key = val;
        left = NULL;
        right = NULL;
    }
};
void HackPrint(HackNode *root){
    if (root == NULL)
        return;
    stack<HackNode *> HackStack;
    HackNode *curr = root;
    while (curr != NULL || HackStack.empty() == false){
        while (curr != NULL){
            cout<<(int)(curr->key)<<" ";
            if (curr->right != NULL)
                HackStack.push(curr->right);
            curr = curr->left;
        }
        if (HackStack.empty() == false){
            curr = HackStack.top();
            HackStack.pop();
        }
    }
}
int main()
{
    HackNode *root = new HackNode('q');
    root->left = new HackNode('w');
    root->right = new HackNode('e');
    root->right->left = new HackNode('r');
    root->right->right = new HackNode('t');
    root->right->right->right = new HackNode('y');
    root->right->right->right->left = new HackNode('u');
    root->right->right->right->right = new HackNode('i');
    HackPrint(root);
}