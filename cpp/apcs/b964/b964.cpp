#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
int main(){
    short int a;
    cin>>a;
    vector<short> l(a);
    for(int i=0;i<a;i++){
        cin>>l[i];
    }
    sort(l.begin(),l.end());
    for(int i:l){
        cout<<i<<" ";
    }
    cout<<endl;
    if(*min_element(l.begin(), l.end())<=60){
        for(int i=a-1;i<a;i--){
            if(l[i]<60){
                cout<<l[i];
                break;
            }
        }
    }
    else{
        cout<<"best case";
    }
    if(*max_element(l.begin(), l.end())>=60){
        cout<<endl<<*lower_bound(l.begin(), l.end(),60);
    }
    else{
        cout<<endl<<"worst case";
    }
}