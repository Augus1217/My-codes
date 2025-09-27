#include<iostream>

using namespace std;
int main()
{
    int a,b;
    cin>>a>>b;
    int s=0;
    s=(a*2+b)%3;
    if (s==0){
        cout<<"普通";
    }
    else if(s==1){
        cout<<"吉";
    }
    else if (s==2){
        cout<<"大吉";
    }
    return 0;
}