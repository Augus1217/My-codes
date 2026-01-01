n,m,k=map(int,input().split())
l=[[int(x) for x in input().split()] for _ in range(n)]
t=[[int(x) for x in input().split()] for _ in range(k)]
ms=1000000
for t in l:
    c=0
    for i in range(n):
        for j in range(m):
            if t[0]==i and t[1]==j:
                c+=l[i][j]
            else:
                if l[i][j]>1000:
                    c+=3000+(l[i][j]-1000)*2
                else:
                    c+=l[i][j]*3
    ms=min(c,ms)
print(ms)
