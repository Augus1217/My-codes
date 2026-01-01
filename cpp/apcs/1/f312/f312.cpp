#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int a1,b1,c1;
    int a2,b2,c2;
    cin>>a1>>b1>>c1;
    cin>>a2>>b2>>c2;
    int n,m=-9999;
    cin>>n;
    for(int x1=0; x1<=n; x1++){
        int x2=n-x1,y1,y2;
        y1=a1*pow(x1,2)+b1*x1+c1;
        y2=a2*pow(x2,2)+b2*x2+c2;
        m=max(y1+y2,m);
    }
    cout<<m<<endl;
}