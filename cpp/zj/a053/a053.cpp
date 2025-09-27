#include<iostream>
using namespace std;
int main()
{
    short int a;
    cin>>a;
    if (a<=10){
        cout<<a*6;
    }
    else if (a<=20){
        cout<<60+((a-10)*2);
    }
    else if (a<=40){
        cout<<80+((a-20));
    }
    else{
        cout<<100;
    }
}