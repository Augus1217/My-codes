#include<iostream>

using namespace std;
int main(){
    string a;
    cin>>a;
    for(int i=0;i<6;i++){
        cout<<abs(a[i+1]-a[i]);
    }
}