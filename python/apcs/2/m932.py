m,n,k=map(int,input().split())
m+=2
n+=2
l=[[-1]*n]
for i in range(m-2):
    l.append([-1]+[i for i in input()]+[-1])
l.append([-1]*n)
move=[int(x) for x in input().split()]
s=''
y,x=m-2,1
for i in move:
    if i==0:
        y-=1
        if l[y][x]==-1:
                y+=1  
                s+=l[y][x]
                continue
    elif i==1:
        x+=1
        if l[y][x]==-1:
                x-=1
                s+=l[y][x]
                continue
    elif i==2:
        y+=1
        x+=1
        if l[y][x]==-1:
                y-=1
                x-=1
                s+=l[y][x]
                continue
    elif i==3:
        y+=1
        if l[y][x]==-1:
                y-=1
                s+=l[y][x]
                continue
    elif i==4:
        x-=1
        if l[y][x]==-1:
                x+=1
                s+=l[y][x]
                continue
    elif i==5:
        y-=1
        x-=1
        if l[y][x]==-1:
                y+=1
                x+=1
                s+=l[y][x]
                continue
    s+=l[y][x]
print(s)
print(len(set(s)))

