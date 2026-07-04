n,m=map(int,input().split())
n+=2
m+=2
l=[[1000000 for _ in range(m)]]
mn=1000000
nl=ml=0
for i in range(n-2):
    cc=[1000000]+[int(i) for i in input().split()]+[1000000]
    l.append(cc)
    if min(cc)<mn:
        mn=min(cc)
        nl, ml = i+1, cc.index(mn)
l.append([1000000 for _ in range(m)])
cnt=mn
while True:
    a=l[nl][ml-1]
    b=l[nl][ml+1]
    c=l[nl-1][ml]
    d=l[nl+1][ml]
    mn=min(a,b,c,d)
    if mn==a and a!=1000000:
        l[nl][ml]=1000000
        ml-=1
    elif mn==b and b!=1000000:
        l[nl][ml]=1000000
        ml+=1
    elif mn==c and c!=1000000:
        l[nl][ml]=1000000
        nl-=1
    elif mn==d and d!=1000000:
        l[nl][ml]=1000000
        nl+=1
    else:
        break
    
    cnt+=mn
print(cnt)