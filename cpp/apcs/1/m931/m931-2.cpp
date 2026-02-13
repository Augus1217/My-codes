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
    int mx1=0,mx2=0;
    int idx1=0,idx2=0;
    for(int i=0; i<n; i++){
        int m = v[i].first;
        int n = v[i].second;
        if(m*m+n*n > mx1){
            mx2 = mx1;
            idx2 = idx1;
            mx1 = m*m+n*n;
            idx1 = i;
        }
        else if(m*m+n*n > mx2){
            mx2 = m*m+n*n;
            idx2 = i;
        }
    }
    cout << v[idx2].first << " " << v[idx2].second;
}