#include<iostream>

using namespace std;
int main(){
    string a;
    cin>>a;
    unsigned short e=0,o=0;
    for(int i=0;i<a.length();i++){
        if(i%2==0){
            o+=a[i]-'0';
        }
        else{
            e+=a[i]-'0';
        }
    }
    cout<<abs(o-e);
}