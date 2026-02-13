

#include <bits/stdc++.h>

using namespace std;

int main() {
    int x,n;
    cin>>x>>n;
    
    int cntL=0;
    int cntR=0;
    int posL=100;
    int posR=-100;
    while(n--){
        int food;
        cin>>food;
        if(food<x){
            cntL++;
        }
        else{
            cntR++;
        }
        posL=min(posL,food);
        posR=max(posR,food);
    }
    if(cntR>cntL){
    cout<<cntR<<" " <<posR ;
    }
    else{
        cout<<cntL<<" " <<posL ;
    }
}
