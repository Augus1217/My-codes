#include<iostream>

using namespace std;
int main()
{
    int n=0;
    while (cin>>n){
        if (n%4==0){
            if(n%100!=0 || n%400==0){
                cout<<"閏年"<<endl;
            }
            else{
                cout<<"平年"<<endl;
            }
        }
        else{
            cout<<"平年"<<endl;
        }
    }
    return 0;
}