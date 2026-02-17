#include<iostream>
#include<vector>
using namespace std;

int main(){
    int r,c,d,k;
    cin>>r>>c>>d>>k;
    vector<pair<int,int>> dm(k);
    vector<vector<int>> map(r, vector<int>(c, d));
    for(int i=0; i<k; i++){
        int a,b;
        cin>>a>>b;
        dm[i]={a,b};
    }
    int m;
    cin>>m;
    vector<vector<int>> pm(m, vector<int>(4));
    for(int i=0; i<m; i++){
        for(int j=0; j<4; j++){
            cin>>pm[i][j];
        }
    }
    for(int i=0; i<m; i++){
        int a=pm[i][0],b=pm[i][1],s=pm[i][2],depth=pm[i][3];
        bool flag=false;
        for (int x=a-s/2; x<a+s/2; x++){
            for (int y=b-s/2; y<b+s/2; y++){
                for (int j=0; j<k; j++){
                    if (dm[j].first==x && dm[j].second==y){
                        dm[j]={-1,-1};
                        flag=true;
                    }
                }
            }
        }
        if (flag==false){
            for (int x=a-s/2; x<a+s/2; x++){
                for (int y=b-s/2; y<b+s/2; y++){
                    if (x>=0 && x<r && y>=0 && y<c){
                        map[x][y]-=depth;
                    }
                }
            }
        }
    }
    int mx = -999;
    int mn = 999;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            int val = map[i][j];
            if (val > mx){
                mx = val;
            }
            if (val < mn){
                mn = val;
            }
        }
    }
    int dc=0;
    for (int i=0; i<k; i++){
        if (dm[i].first!=-1 && dm[i].second!=-1){
            dc++;
        }
    }
    cout<<mx<<" "<<mn<<" "<<dc<<endl;
    return 0;
}