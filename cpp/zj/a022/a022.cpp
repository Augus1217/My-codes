#include<iostream>

using namespace std;
int main()
{
    string a;
    cin>>a;
    bool f=false;
    for(short int i=0;i<a.length()/2;i++){
        if(a[i]!=a[a.length()-i-1]){
            f=true;
            break;
        }
    }
    if(f==false){
        cout<<"yes";
    }
    else{
        cout<<"no";
    }
}