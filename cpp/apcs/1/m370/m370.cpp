#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int x,n;
    cin >> x >> n;
    vector<int> v(n);
    for (int i=0; i<n; i++){
        cin >> v[i];
    }
    sort(v.begin(),v.end());
    int c1=0,c2=0;
    for (int i : v){
        if (i>x){
            c1+=1;
        }
        else if (i<x){
            c2+=1;
        }
    }
    int b;
    if (c1>c2){
        b=v[n-1];
        cout << c1 << " " << b << endl;
    }
    else{
        b=v[0];
        cout << c2 << " " << b << endl;
    }
}