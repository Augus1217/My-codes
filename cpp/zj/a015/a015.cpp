#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int r,c;
    while(cin>>r>>c){
        int l[r][c];
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                cin>>l[i][j];
            }
        }
        for(int i=0;i<c;++i){
            for(int j=0;j<r;++j){
                cout<<l[j][i]<<" ";
            }
            cout<<endl;
        }
    }
}