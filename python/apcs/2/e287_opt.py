from collections import deque

n, m = map(int, input().split())  # 地圖維度 n*m
graph = []  # 地圖
now = 10000000  # 目前的最小值，預設為大於題目範圍的值
sr, sc = 0, 0  # 起點，預設為 (0, 0)
for i in range(n):  # 讀取 n 行資料
    row = list(map(int, input().split()))  # 讀取一行資料
    graph.append(row)  # 加到 graph
    imin = min(row)  # 此行中的最小值
    if imin < now:  # 如果 imin < now
        now = imin  # 更新 now
        sr, sc = i, row.index(imin)  # 更新起點座標
# end of for loop
que = deque(); que.append([sr, sc])  # 待走訪節點
total = 0  # 加總
visit = [[False]*m for _ in range(n)]  # 走訪狀態
# BFS
while que:  # 如果 que 還有資料繼續執行
    r, c = que.popleft()  # 從 que 最前面讀取並移除資料
    visit[r][c] = True  # 已走訪 (r, c)
    total += graph[r][c]  # 更新 total
    imin = 10000000  # 暫存最小值的變數
    for dr, dc in ((0, 1), (-1, 0), (0, -1), (1, 0)):  # 四方向檢測
        nr, nc = r+dr, c+dc  # 要測試的座標 (nr, nc)
        if nr < 0 or nr >= n or nc < 0 or nc >= m: continue  # 如果 (nr, nc) 已出界，檢測下一個點
        if visit[nr][nc]: continue  # 如果 (nr, nc) 已走訪，檢測下一個點
        if graph[nr][nc] < imin:  # 如果 (nr, nc) 的值小於 imin
            if imin == 10000000: que.append([nr, nc])  # 如果 imin 等於 10000000，找到四方向中第一個值，[nr, nc] 加入 que
            else: que[-1] = [nr, nc]  # 否則取代 que 最後一項
            imin = graph[nr][nc]  # 更新 imin
    # 結束四方向檢測
# end of while loop
print(total)  # 印出答案