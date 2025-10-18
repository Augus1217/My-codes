#include<iostream>
using namespace std;
int main(){
        int k,x1,x2,y1,y2,p=0;
        cin>>k>>x1>>y1>>x2>>y2;
        while (k>0){
                p+=k;
                if(p%x1==0){
                        k-=y1;
                }
                if(p%x2==0){
                        k-=y2;
                }
        }
        cout<<p;
        return 0;
}
