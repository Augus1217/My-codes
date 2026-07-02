d={} # 儲存字串及其相異字元數
d2={} # 儲存相異字元數最少的字串
s=int(input()) # 讀取輸入的字串數量
for i in range(s):
    t=input() # 讀取字串
    d[t]=len(set(t)) # 計算該字串的相異字元數量，並存入字典 d
n=min(list(d.values())) # 找出最少的相異字元數量
for k,v in d.items():
    if v==n: # 如果該字串的相異字元數量等於最小值
        d2[k]=v # 將其加入 d2
d={}
for i in sorted(d2): # 對 d2 的鍵 (字串) 進行排序 (字典序)
    d[i]=d2[i]
print(list(d.keys())[0]) # 印出排序後的第一個字串