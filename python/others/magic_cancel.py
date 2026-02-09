# 尋找「錯誤消去法」卻剛好得到正確答案的分數 (兩位數)
# 例如 16/64 => 把 6 消掉 => 1/4 (數值相等)

print("正在尋找兩位數中，這套「歪理」剛好會矇對的例子：\n")

results = []

for n in range(10, 100):
    for d in range(n + 1, 100): # d > n，只找真分數
        n_str = str(n)
        d_str = str(d)
        
        # 1. 排除 10/20, 20/30 這種單純消 0 的無趣例子
        # 影片如果是講「消去相同的數字」，觀眾通常不接受消 0 (那是約分)
        if '0' in n_str or '0' in d_str:
            continue
            
        # 2. 找出分子分母共有的數字
        common_digits = set(n_str) & set(d_str)
        
        if not common_digits:
            continue
            
        for digit in common_digits:
            # 模擬「錯誤消去」：從字串中移除該數字
            # 注意：這裡只移除「一個」該數字，模擬劃掉的動作
            n_list = list(n_str)
            d_list = list(d_str)
            
            try:
                n_list.remove(digit)
                d_list.remove(digit)
                
                # 剩下的數字
                new_n = int(n_list[0])
                new_d = int(d_list[0])
                
                if new_d == 0: continue # 分母不能為 0
                
                # 檢查數值是否相等
                # 使用交叉相乘避免浮點數誤差: n/d == new_n/new_d  =>  n*new_d == d*new_n
                if n * new_d == d * new_n:
                    results.append(f"{n}/{d} (等於 {n/d:.2f}) -> 劃掉 {digit} -> {new_n}/{new_d} (等於 {new_n/new_d:.2f})")
            except ValueError:
                continue

if results:
    for res in results:
        print(f"找到巧合！: {res}")
else:
    print("找不到任何巧合。")
