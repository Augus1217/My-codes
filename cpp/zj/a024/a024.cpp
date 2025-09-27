#include<iostream>

using namespace std;
int main()
{
    unsigned int a,b;
    cin>>a>>b;
    while(true){
        if(a<b){
            swap(a,b);
        }
        a=a%b;
        if(a==0){
            break;
        }
    }
    cout<<b;
}