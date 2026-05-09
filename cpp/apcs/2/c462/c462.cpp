#include<iostream>
#include<string>
#include<cctype>
#include<vector>
using namespace std;
int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> v;
    for (char c : s){
        if (isupper(c)){
            v.push_back(1);
        }
        else{
            v.push_back(0);
        }
    }
    vector<int> l;
    int c=1;
    for (int i=0; i < v.size()-1; i++){
        if (v[i] == v[i+1]){
            c++;
        }
        else{
            l.push_back(c);
            c=1;
        }
    }
    l.push_back(c);
    int mx=0,x=0;
    for (int i=0; i < l.size(); i+=1){
        if (l[i]==n){
            x+=n;
        }
        else if(l[i]>n){
            x+=n;
            if (x > mx){
                mx = x;
            }
            x=n;
        }
        else{
            if (x > mx){
                mx = x;
            }
            x=0;
        }
    }
    if (x > mx){
        mx = x;
    }
    cout << mx << endl;
    return 0;
}