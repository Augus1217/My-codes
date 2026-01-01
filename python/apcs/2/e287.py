n,m=map(int,input().split())
n+=2
m+=2
l=[[1000001]*m]
for i in range(n-2):
    l.append([1000001]+[int(i) for i in input().split()]+[1000001])
l.append([1000001]*m)
oo=1000001
mm=oo
for i in range(1,n-1):
    for j in range(1,m-1):
        if l[i][j]<mm:
            mm=l[i][j]
            y,x,s=i,j,mm
t=0
while True:
    up=y-1
    down=y+1
    left=x-1
    right=x+1
    if min(l[down][x],l[y][left],l[y][right],l[up][x])==1000001:
        t+=l[y][x]
        break
    elif l[up][x]==min(l[down][x],l[y][left],l[y][right],l[up][x]):
        t+=l[y][x]
        l[y][x]=1000001
        y-=1
    elif l[down][x]==min(l[down][x],l[y][left],l[y][right],l[up][x]):
        t+=l[y][x]
        l[y][x]=1000001
        y+=1
    elif l[y][left]==min(l[down][x],l[y][left],l[y][right],l[up][x]):
        t+=l[y][x]
        l[y][x]=1000001
        x-=1
    elif l[y][right]==min(l[down][x],l[y][left],l[y][right],l[up][x]):
        t+=l[y][x]
        l[y][x]=1000001
        x+=1
print(t)
