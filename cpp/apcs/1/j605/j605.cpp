#include <iostream>
using namespace std;

int main(){
    int k,ms=-1,mt=0,ec=0;
    cin >> k;
    for(int i = 0; i < k; i++){
        int t,s;
        cin >> t >> s;
        if (s==-1){
            ec++;
        }
        else if (s>ms){
            ms=s;
            mt=t;
        }
    }
    int sc=ms-k-2*ec;
    if (sc<0){
        sc=0;
    }
    cout << sc << " " << mt << endl;
}