#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int x1,y1,x2,y2;
    int l=0,r=0,t=0;
    char d='E';
    cin >> x1 >> y1;
    for(int i=0; i<n-1; i++){
        cin >> x2 >> y2;
        switch(d){
            case 'E':
                if (y2>y1){
                    l+=1;
                    d='N';
                }
                else if (y2<y1){
                    r+=1;
                    d='S';
                }
                else if (x2<x1){
                    t+=1;
                    d='W';
                }
                break;
            case 'W':
                if (y2>y1){
                    r+=1;
                    d='N';
                }
                else if (y2<y1){
                    l+=1;
                    d='S';
                }
                else if (x2>x1){
                    t+=1;
                    d='E';
                }
                break;
            case 'N':
                if (x2>x1){
                    r+=1;
                    d='E';
                }
                else if (x2<x1){
                    l+=1;
                    d='W';
                }
                else if (y2<y1){
                    t+=1;
                    d='S';
                }
                break;
            case 'S':
                if (x2>x1){
                    l+=1;
                    d='E';
                }
                else if (x2<x1){
                    r+=1;
                    d='W';
                }
                else if (y2>y1){
                    t+=1;
                    d='N';
                }
                break;
        }
        x1=x2;
        y1=y2;
    }
    cout << l << " " << r << " " << t << endl;
}