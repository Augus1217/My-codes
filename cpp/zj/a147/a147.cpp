#include<iostream>

using namespace std;
int main(){
    short int a=1;
    while(a!=0){
        cin>>a;
        for(short int i=0;i<a;i++){
            if(i%7!=0){
                cout<<i<<" ";
            }
        }
        cout<<endl;
    }
}