#include<iostream>

using namespace std;
int main(){
    short d,e;
    bool a,b,c,f=false;
    cin>>d>>e>>c;
    a=!!d;
    b=!!e;
    if((a&&b)==c){
        cout<<"AND"<<endl;
        f=true;
    }
    if((a||b)==c){
        cout<<"OR"<<endl;
        f=true;
    }
    if((a^b)==c){
        cout<<"XOR"<<endl;
        f=true;
    }
    if(f==false){
        cout<<"IMPOSSIBLE";
    }
}