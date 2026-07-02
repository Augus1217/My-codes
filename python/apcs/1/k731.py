n=int(input())
x=0
y=0
f=0
d=[0]*3
for i in range(n):
    px,py=map(int,input().split())
    if px-x>0:
        if f=='N':
            d[1]+=1
        elif f=='S':
            d[0]+=1
        elif f=='W':
            d[2]+=1
        f='E'
    elif py-y>0:
        if f=='S':
            d[2]+=1
        elif f=='E':
            d[0]+=1
        elif f=='W':
            d[1]+=1
        f='N'
    elif px-x<0:
        if f=='N':
            d[0]+=1
        elif f=='S':
            d[1]+=1
        elif f=='E':
            d[2]+=1
        f='W'
    elif py-y<0:
        if f=='N':
            d[2]+=1
        elif f=='E':
            d[1]+=1
        elif f=='W':
            d[0]+=1
        f='S'

    x=px
    y=py

print(*d)