#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<pair<int, int>> v;
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
    int mx=0,mxl;
    for(int i=0; i<n; i++){
        int m = v[i].first;
        int n = v[i].second;
        if(m*m+n*n > mx){
            mx = m*m+n*n;
            mxl = i;
        }
    }
    v[mxl]={0,0};
    mx=0;
    for(int i=0; i<n; i++){
        int m = v[i].first;
        int n = v[i].second;
        if(m*m+n*n > mx){
            mx = m*m+n*n;
            mxl = i;
        }
    }
    cout << v[mxl].first << " " << v[mxl].second;
}