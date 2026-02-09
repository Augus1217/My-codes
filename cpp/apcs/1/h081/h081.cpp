#include<iostream>
using namespace std;
int main(){
    int x=-1,n,d,c,a=0;
    int l[100];
    cin>>n>>d;
    for(int i=0;i<n;i++){
        cin>>l[i];
    }
    c=l[0];
    for(int i=1;i<n;i++){
        if(l[i]>=c+d && c!=-1){ // sell
            a+=l[i]-c;
            c=-1;
            x=l[i];

        }
        else if (l[i]<=x-d && c==-1){ // buy
            c=l[i];
        }
    }
    cout<<a;
    return 0;
}