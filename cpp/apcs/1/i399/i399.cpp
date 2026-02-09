#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
using namespace std;

int main(){
    vector<int> l, times(10,0);
    set<int, greater<int>> s;
    int mc=0;
    for(int i=0; i<3; i++){
        int a;
        cin >> a;
        l.push_back(a);
        s.insert(a);
    }
    for(int i=0; i<3; i++){
        times[l[i]]++;
    }
    for(int i:times){
        mc=max(mc,i);
    }
    cout << mc;
    for(int i:s){
        cout<<" "<<i;
    }
    return 0;
}