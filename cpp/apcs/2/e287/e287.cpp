#include<iostream>
using namespace std;
int main(){
    int n,m,mi,mj,mv=1000000;
    cin >> n >> m;
    n+=2;
    m+=2;
    int l[n][m];
    for (int i=0; i < n; i++){
        for (int j=0; j < m; j++){
            l[i][j] = 1000001;
        }
    }
    for (int i=1; i < n-1; i++){
        for (int j=1; j < m-1; j++){
            cin >> l[i][j];
            if (l[i][j] < mv){
                mv = l[i][j];
                mi = i;
                mj = j;
            }
        }
    }
    int c=mv;
    int a=mi,b=mj;
    l[a][b]=1000001;
    while(true){
        int up=l[a-1][b];
        int down=l[a+1][b];
        int left=l[a][b-1];
        int right=l[a][b+1];
        int mnvl=min(up,min(down,min(left,right)));
        if (mnvl == 1000001){
            break;
        }
        else if (mnvl == up){
            l[a-1][b]=1000001;
            a-=1;
        }
        else if (mnvl == down){
            l[a+1][b]=1000001;
            a+=1;
        }
        else if (mnvl == left){
            l[a][b-1]=1000001;
            b-=1;
        }
        else if (mnvl == right){
            l[a][b+1]=1000001;
            b+=1;
        }
        c+=mnvl;
    }
    cout << c << endl;
    return 0;
}