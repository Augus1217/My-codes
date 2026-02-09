#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

int main(){
    vector<pair<int, int>> v;
    int n, mx=-999, mn=999;
    cin >> n;
    for(int i=0; i<n; i++){
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
    for(int i=0; i<n-1; i++){
        int x=abs(v[i].first-v[i+1].first);
        int y=abs(v[i].second-v[i+1].second);
        if (x+y > mx) {
            mx = x+y;
        }
        if (x+y < mn) {
            mn = x+y;
        }
    }
    cout << mx << " " << mn;
    return 0;
}