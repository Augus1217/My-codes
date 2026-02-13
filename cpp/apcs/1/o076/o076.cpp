#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    vector<int> v;
    cin >> n;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    int mx=0,x=1;
    for(int i=0; i<n-1; i++){
        if(v[i] > v[i+1]){
            x+=1;
        }
        else{
            mx = max(mx, x);
            x=1;
        }
    }
    mx = max(mx, x);
    cout << mx;
}