n,m=map(int,input().split())
n+=2
m+=2
s=0
f=True
l=[[-1]*m]
for i in range(n-2):
    l.append([-1]+[int(x) for x in input().split()]+[-1])
l.append([-1]*m)
while f==True:
    f=False
    for i in range(1,n-1):
        for j in range(1,m-1):
            if l[i][j]==-1:
                continue
            x=-1
            c=0
            for k in range(1,j):
                x=l[i][j-k]
                if x!=-1:
                    c=k
                    break
            if x==l[i][j]:
                l[i][j-c],l[i][j]=-1,-1
                s+=x
                f=True
                continue
            for k in range(1,i):
                x=l[i-k][j]
                if x!=-1:
                    c=k
                    break
            if x==l[i][j]:
                l[i-c][j],l[i][j]=-1,-1
                s+=x
                f=True
                continue
print(s)
