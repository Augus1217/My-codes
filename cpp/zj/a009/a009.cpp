#include<iostream>

using namespace std;
int main()
{
    string a;
    cin>>a;
    for(short int i=0;i<a.length();i++){
        cout<<char(int(a[i])-7);
    }
}