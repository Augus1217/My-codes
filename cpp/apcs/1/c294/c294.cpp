#include<iostream>
#include<algorithm>

using namespace std;
int main(){
    short l[3];
    cin>>l[0]>>l[1]>>l[2];
    sort(l,l+3);
    cout<<l[0]<<' '<<l[1]<<' '<<l[2]<<endl;
    if(l[0]+l[1]<=l[2]){
        cout<<"No";
    }
    else if(l[0]*l[0]+l[1]*l[1]<l[2]*l[2]){
        cout<<"Obtuse";
    }
    else if(l[0]*l[0]+l[1]*l[1]==l[2]*l[2]){
        cout<<"Right";
    }
    else{
        cout<<"Acute";
    }
}