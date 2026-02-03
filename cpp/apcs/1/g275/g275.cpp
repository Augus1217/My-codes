#include<iostream>
using namespace std;
int main(){
    int n=0;
    cin>>n;
    for (int i=0;i<n;i++){
        cout<<endl;
        int a[7],b[7];
        bool flag=false;
        for(int j=0;j<7;j++){
            cin>>a[j];
        }
        for(int j=0;j<7;j++){
            cin>>b[j];
        }
        if (a[1]==a[3] || a[1]!=a[5] || b[1]==b[3] || b[1]!=b[5]){
            cout<<"A";
            flag=true;
        }
        if (a[6]!=1 || b[6]!=0){
            cout<<"B";
            flag=true;
        }
        if (a[1]==b[1] || a[3]==b[3] || a[5]==b[5]){
            cout<<"C";
            flag=true;
        }
        if (flag==false){
            cout<<"None";
        }
    }
    return 0;
}