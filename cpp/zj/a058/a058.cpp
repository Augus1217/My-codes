#include<iostream>

using namespace std;
int main(){
    short int n;
    short int l[3]={0,0,0};
    unsigned short int a;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
        if(a%3==0){
            l[0]+=1;
        }
        else if(a%3==1){
            l[1]+=1;
        }
        else{
            l[2]+=1;
        }
    }
    cout<<l[0]<<" "<<l[1]<<" "<<l[2];
}