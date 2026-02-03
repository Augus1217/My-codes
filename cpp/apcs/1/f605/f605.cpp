#include<iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,d,c=0,r=0;
    cin>>n>>d;
    int l[3];
    for(int i=0;i<n;i++){
        cin>>l[0]>>l[1]>>l[2];
        if (max({l[0],l[1],l[2]}) - min({l[0],l[1],l[2]}) >= d){
            r+=1;
            c+=(l[0]+l[1]+l[2])/3;
        }
    }
    cout<<r<<" "<<c;
    return 0;
}