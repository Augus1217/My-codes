#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    
    // 儲存每個人的下家是誰 (索引 i 的人交給 friends[i])
    vector<int> friends(n);
    for(int i = 0; i < n; i++){
        cin >> friends[i];
    }
    
    // visited 陣列就是「貼紙」，false 代表沒來過，true 代表來過了
    vector<bool> visited(n, false);
    int groups = 0; // 幾個群體
    
    // 從 0 號同學開始檢查到最後一個
    for (int i = 0; i < n; i++){
        // 如果這個人還沒被貼過貼紙 (代表他是一個新群體的起頭)
        if (!visited[i]) {
            int current = i; // 從他開始走
            
            // 只要現在走到的人還沒被貼過貼紙，就繼續走
            while (!visited[current]) {
                visited[current] = true;   // 1. 貼上貼紙 (標記已拜訪)
                current = friends[current];// 2. 走到下一個人那裡
            }
            // 當 while 結束，代表走到一個已經被貼過貼紙的人身上
            // 因為題目保證每個人只會指一人且被一人指，所以一定只會繞回自己這個群體的人
            // 代表這一個圈圈走完了
            
            groups++; // 群體數量 + 1
        }
    }
    
    cout << groups << endl;
    return 0;
}