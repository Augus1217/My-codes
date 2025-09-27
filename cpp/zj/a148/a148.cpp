#include <iostream>

using namespace std;
int main(){
    unsigned int a,b=0,c;
    while(cin>>a){
        for(int i=0;i<a;i++){
            cin>>c;
            b+=c;
        }
        if(b/a<60){
            cout<<"no"<<endl;
        }
        else{
            cout<<"yes"<<endl;
        }
        b=0;
    }
}