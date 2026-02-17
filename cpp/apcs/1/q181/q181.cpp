#include<iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int n;
    cin >> n;
    int cc=0;
    for (int i=0; i<n; i++) {
        int x, c=0;
        cin >> x;
        x%=a+b;
        x-=a;
        if (x<0){
            c=0;
        }
        else{
            c+=b-x;
        }
        cc+=c;
    }
    cout << cc << endl;
    return 0;
}