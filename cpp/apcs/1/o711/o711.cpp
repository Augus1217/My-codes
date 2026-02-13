#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    int w1,w2,h1,h2;
    cin >> w1 >> w2 >> h1 >> h2;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        v[i] = a;
    }
    int m1 = w1*w1*h1, m2 = w2*w2*h2;
    int curm1 = m1, curm2 = m2;
    int mx=0;
    for(int i=0; i<n; i++){
        if (v[i]>curm1){
            v[i] -= curm1;
            curm1 = 0;
            if (v[i]>curm2){
                v[i] -= curm2;
                curm2 = 0;
            }
            else{
                curm2 -= v[i];
                v[i] = 0;
            }
        }
        else{
            curm1 -= v[i];
            v[i] = 0;
        }
        int d=(m1-curm1)/w1/w1 + (m2-curm2)/w2/w2;
        if (d>mx){
            mx = d;
        }
        m1=curm1;
        m2=curm2;
    }
    cout << mx << endl;
    return 0;
}