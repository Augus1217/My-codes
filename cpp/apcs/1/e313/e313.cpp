#include<set>
#include<iostream>
#include<vector>
using namespace std;
int main(){
    short int n, ma=32767; // n: 字串數量, ma: 目前最小的相異字元數 (初始設為最大值)
    string ms; // ms: 目前符合條件(相異字元數最少且字典序最小)的字串
    cin>>n; // 輸入 n
    vector<string> l(n); // 宣告字串向量
    for(int i=0;i<n;i++){
        cin>>l[i]; // 輸入字串
        set<char> s; // 宣告字元集合，用來計算該字串的相異字元數
        for(int j=0;j<l[i].size();j++){ // 遍歷字串中的每個字元
            s.insert(l[i][j]); // 將字元加入集合 (重複的會被忽略)
        }
        if(s.size() < ma){ // 如果目前的相異字元數比紀錄的最小值還小
            ma = s.size(); // 更新最小值
            ms = l[i]; // 更新答案字串
        } else if(s.size() == ma){ // 如果相異字元數等於最小值
            if(ms == "" || l[i] < ms){ // 比較字典序，若目前的字串較小
                ms = l[i]; // 更新答案字串
            }
        }
    }
    cout << ms << endl; // 輸出最終結果
    return 0;
}