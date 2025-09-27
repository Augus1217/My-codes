#include <iostream>
#include <unordered_map>
#include <string>
#include <chrono>

int main() {
    // 創建一個無序映射 (unordered_map)，相當於 Python 的字典
    // 對於大型集合，unordered_map 通常比 map 更快
    std::unordered_map<int, std::string> l;

    // 填充映射，這裡使用 1000 萬個元素以獲得更合理的執行時間
    // 注意：1 億個元素會消耗大量記憶體，可能導致程式崩潰
    std::cout<<"初始化中..."<<std::endl;
    for (int i = 0; i < 100; ++i) {
        std::cout<<i<<"%"<<std::endl;
        for (int j = 0; j < 100000; ++j) {
            l[j*i] = "1";
        }
    }

    std::cout<<"100%"<<std::endl;
    int accu;
    std::cout << "輸入帳號: ";
    std::cin >> accu;

    std::cout << "開始尋找..." << std::endl;

    // 記錄開始時間
    auto st = std::chrono::high_resolution_clock::now();

    std::string passw = "",cinpassw="";

    // 使用 find 方法直接查找鍵，這遠比遍歷整個映射高效
    // find 方法會回傳一個 iterator（迭代器），如果找到對應的鍵，iterator 會指向該元素；
    // 如果找不到，iterator 會等於 l.end()，表示查無此鍵。
    auto it = l.find(accu);
    if (it == l.end()) {
        std::cout << "帳號不存在，程式結束。" << std::endl;
        return 1;
    } else {
        passw = it->second;
    }

    // 記錄結束時間
    auto et = std::chrono::high_resolution_clock::now();

    // 計算經過的時間
    std::chrono::duration<double> elapsed = et - st;
    std::cout<<"請輸入密碼: ";
    std::cin>>cinpassw;
    while(cinpassw!=passw){
        std::cout<<"密碼錯誤，請再試一次: ";
        std::cin>>cinpassw;
    }
    std::string logout="";
    std::cout<<"歡迎使用，輸入logout來結束程式"<<std::endl;
    while(true){
        std::cin>>logout;
        if(logout=="logout"){
                break;
                std::cout<<"程式結束"<<std::endl;
        }
    }
    return 0;
}
