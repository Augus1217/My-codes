#include<iostream>

using namespace std;

short int a[10000001];
int main()
{
    long long int c=0,n,l,r;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>l>>r;
        for (int j=l;j<r;j++){
            a[j]=1;
        }
    }
    for (int i=0;i<10000000;i++){
        if (a[i]==1){
            c+=1;
        }
    }
    cout<<c;
    return 0;
}