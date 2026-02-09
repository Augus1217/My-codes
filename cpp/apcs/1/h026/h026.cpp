#include<iostream>
using namespace std;
int main(){
    int f,n,c=0;
    string flag="Drew";
    cin>>f;
    cin>>n;
    int l[10], fl[10];
    for(int i=0;i<n;i++){
        cin>>l[i];
    }
    for(int i=0;i<n;i++){
        c++;
        fl[i]=f;
        if(l[i]==0){
            if(f==2){
                flag="Lost";
                break;
            }
            else if(f==5){
                flag="Won";
                break;
            }
        }
        else if(l[i]==2){
            if(f==0){
                flag="Won";
                break;
            }
            else if(f==5){
                flag="Lost";
                break;
            }
        }
        else if(l[i]==5){
            if(f==0){
                flag="Lost";
                break;
            }
            else if(f==2){
                flag="Won";
                break;
            }
        }
        if(i>=1){
            if(l[i]==l[i-1]){
                if (l[i]==0){
                    f=5;
                }
                else if(l[i]==2){
                    f=0;
                }
                else{
                    f=2;
                }
            }
            else{
                f=l[i];
            }
        }
        else{
            f=l[i];
        }
    }
    for(int i=0;i<c;i++){
        cout<<fl[i]<<" ";
    }
    cout<<": "<<flag<<" at round "<<c;
    return 0;

}