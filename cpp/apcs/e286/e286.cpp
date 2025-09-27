#include<iostream>
using  namespace std;
int main(){
    int m1[4],n1[4],m2[4],n2[4];
    int nm1=0,nn1=0,nm2=0,nn2=0;
    bool p1,p2;
    cin>>m1[0]>>m1[1]>>m1[2]>>m1[3];
    cin>>n1[0]>>n1[1]>>n1[2]>>n1[3];
    cin>>m2[0]>>m2[1]>>m2[2]>>m2[3];
    cin>>n2[0]>>n2[1]>>n2[2]>>n2[3];
    for(int i=0;i<4;i++){
        nm1+=m1[i];
        nn1+=n1[i];
        nm2+=m2[i];
        nn2+=n2[i];
    }
    if(nm1>nn1){
        p1=true;
    }
    else{
        p1=false;
    }
    if(nm2>nn2){
        p2=true;
    }
    else{
        p2=false;
    }
    cout<<nm1<<':'<<nn1<<endl;
    cout<<nm2<<':'<<nn2<<endl;
    if(p1==true && p2==true){
        cout<<"Win";
    }
    else if(p1==false && p2==false){
        cout<<"Lose";
    }
    else{
        cout<<"Tie";
    }
}