#include <bits/stdc++.h>
using namespace std;

// 大樓高度
int h[100];

// 判斷大樓 l 到大樓 r 是否可以滑翔 (是否嚴格遞減)
bool ok(int l, int r) {
    for (int i = l; i <= r-1; i++) {
        if (h[i + 1] >= h[i]) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) cin >> h[i];
    // 嘗試每一對 l r
    for (int l = 1; l <= n; l++) {
        for (int r = l + 1; r <= n; r++) {
            // 檢查是否合法，如果合法就嘗試更新答案
            if (ok(l, r)) ans = max(ans, r - l + 1);
        }
    }
    // 輸出答案
    cout << ans << endl;
}
