#include<iostream>
using namespace std;
int main(){
    int n,f,b,c=0;
    cin>>n;
    int l[100];
    for(int i=0;i<n;i++){
        cin>>l[i];
    }
    for(int i=0;i<n;i++){
        if(l[i]==0){
            if(i!=0){
                f=l[i-1];
            }
            else{
                f=101;
            }
            if(i!=n-1){
                b=l[i+1];
            }
            else{
                b=101;
            }
            if(f<b){
                c+=f;
            }
            else{
                c+=b;
            }
        }
    }
    cout<<c;
    return 0;
}