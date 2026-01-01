r,c,k,m=map(int,input().split())
r+=2
c+=2
l=[[-1]*c]
for _ in range(r-2):
    l.append([-1]+[int(x) for x in input().split()]+[-1])
l.append([-1]*c)
l2=[[0]*c for _ in range(r)]
for _ in range(m):
    for i in range(1,r-1):
        for j in range(1,c-1):
            l2[i][j]=l[i][j]
            if l[i][j]==-1:
                continue
            if l[i+1][j]!=-1:
                l2[i][j]+=l[i+1][j]//k-l[i][j]//k
            if l[i-1][j]!=-1:
                l2[i][j]+=l[i-1][j]//k-l[i][j]//k
            if l[i][j+1]!=-1:
                l2[i][j]+=l[i][j+1]//k-l[i][j]//k
            if l[i][j-1]!=-1:
                l2[i][j]+=l[i][j-1]//k-l[i][j]//k
    l=l2

print(l)
s=9999
b=0
for i in range(1,r-1):
    for j in range(1,c-1):
        if l[i][j]>b:
            b=l[i][j]
        if 0<=l[i][j]<s:
            s=l[i][j]
print(s)
print(b)
