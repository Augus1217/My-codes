r,c,d=map(int,input().split())
k=int(input())
l=[]
for i in range(k):
    l.append(list(map(int,input().split())))
m=int(input())
pl=[]
for i in range(m):
    pl.append(list(map(int,input().split())))
mp=[[d for j in range(c)] for i in range(r)]
flag=False
for i in range(m):
    a,b=pl[i][0],pl[i][1]
    s=pl[i][2]
    pd=pl[i][3]
    for j in range(a-s//2,a+s//2+1):
        for k in range(b-s//2,b+s//2+1):
                while [j,k] in l:
                    del l[l.index([j,k])]
                    flag=True
    if not flag:
        for j in range(a-s//2,a+s//2+1):
            for k in range(b-s//2,b+s//2+1):
                if j>=0 and j<r and k>=0 and k<c:
                    try:
                        mp[j][k]-=pd
                    except:
                        pass
    flag=False
mx=-9999999
mn=9999999
for i in range(r):
    if max(mp[i])>mx:
        mx=max(mp[i])
    if min(mp[i])<mn:
        mn=min(mp[i])
print(mx,mn,len(l))