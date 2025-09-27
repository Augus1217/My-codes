#include<iostream>

using namespace std;
int main()
{
    short int a;
    int l[4];
    cin>>a;
    for(int i=0;i<a;i++){
        cin>>l[0]>>l[1]>>l[2]>>l[3];
        if((l[1]-l[0])==(l[2]-l[1]) && (l[2]-l[1])==(l[3]-l[2])){
            cout<<l[0]<<" "<<l[1]<<" "<<l[2]<<" "<<l[3]<<" "<<l[3]+(l[1]-l[0])<<endl;
        }
        else{
            cout<<l[0]<<" "<<l[1]<<" "<<l[2]<<" "<<l[3]<<" "<<l[3]*(l[1]/l[0])<<endl;
        }
    }
    return 0;
}