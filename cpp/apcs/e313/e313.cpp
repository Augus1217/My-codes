#include<set>
#include<iostream>
#include<vector>
using namespace std;
int main(){
    short int n,x,ma=32767;
    string ms;
    cin>>n;
    vector<string> l(n);
    set<string> s;
    for(int i=0;i<n;i++){
        cin>>l[i];
        for(int j=0;j<l.size();j++){
            s.insert(l[i]);
        }
        if(ma>s.size()){
            
        }
    }
}