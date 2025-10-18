
#include<iostream>
#include <cmath>

using namespace std;
int main()
{
    int a,b,d=0,e=0;
    short int c;
    bool f=false;
    cin>>a>>b;
    for(int i=a;i<b;i++){
        e=i;
        c=floor(log10(i)+1);
        while(e!=0){
            d+=pow(e%10,c);
            e/=10;
        }
        if(d==i){
            cout<<i<<" ";
            f=true;
        }
        d=0;
    }
    if(f==false){
        cout<<"none";
    }
    return 0;
}