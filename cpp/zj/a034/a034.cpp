#include<iostream>
#include <string>
#include <algorithm>

using namespace std;
int main()
{    
    int a;
    while(cin>>a){
        string c;
        char b;
        while(a>0){
            b=static_cast<char>(a%2+'0');
            c=c+b;
            a/=2;
        }
        reverse(c.begin(),c.end());
        cout<<c<<endl;
    }
}