#include <iostream>
#include <algorithm> // 為了用 max()
using namespace std;

int main() {
    // 優化輸入輸出速度 (非必要但習慣加上)
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    int w1, w2, h1, h2;
    // 輸入 n 和杯子的參數
    cin >> n;
    cin >> w1 >> w2 >> h1 >> h2;

    int max_delta = 0; // 紀錄 n 次中，上升變化量最大的那次

    for (int i = 0; i < n; i++) {
        int water;
        cin >> water; // 這次倒進去的水量 (體積)
        
        int delta = 0; // 這次倒水讓水位上升了多少 (本輪的答案)

        // 步驟 1: 先看下面那層 (w1, h1) 還能不能裝
        // 下層還有空間 (h1 > 0)
        if (h1 > 0) {
            // 計算這次的水，如果全部倒進下層，會佔用多少高度
            // 體積 / 底面積 = 高度
            int height_needed = water / (w1 * w1);

            if (height_needed <= h1) {
                // 情況 A: 下層夠裝，且沒滿 (或剛好滿)
                delta += height_needed;
                h1 -= height_needed;   // 下層剩餘空間變少
                water = 0;             // 水都倒完了
            } else {
                // 情況 B: 下層不夠裝，會溢到上層
                delta += h1;           // 水位上升量 = 下層剩下的所有高度
                water -= (w1 * w1) * h1; // 水還沒倒完，扣掉填滿下層用掉的體積
                h1 = 0;                // 下層滿了 (剩餘高度為 0)
            }
        }

        // 步驟 2: 如果水還沒倒完 (water > 0)，且下層已滿 (h1 == 0)，就要倒進上層
        if (water > 0 && h1 == 0) {
            // 計算剩下的水，在上層會佔用多少高度
            int height_needed = water / (w2 * w2);

            if (height_needed <= h2) {
                // 情況 C: 上層夠裝，且沒滿
                delta += height_needed;
                h2 -= height_needed;   // 上層剩餘空間變少
                water = 0;
            } else {
                // 情況 D: 上層也不夠裝，滿出來了 (溢出杯子)
                // 題目雖未明說溢出怎麼算，但通常算到滿為止
                delta += h2;           // 水位上升量 = 上層剩下的所有高度
                h2 = 0;                // 上層也滿了
                water = 0;             // 多出來的水流掉了，不用管它
            }
        }

        // 更新歷史最大值
        max_delta = max(max_delta, delta);
    }

    cout << max_delta << endl;

    return 0;
}
