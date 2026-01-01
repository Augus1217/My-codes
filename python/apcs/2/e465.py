m,s,n=map(int,input().split())
l=sorted([int(x) for x in input().split()])
s-=(m-sum(l))
min=99999
a=0
if s<=0:
    print(0)
else:
    for i in range(n):
        for j in range(i,n):
            if abs(s-sum(l[i:j+1]))<=min:
                min=abs(s-sum(l[i:j+1]))
                a=sum(l[i:j+1])
        for j in range(n,i,-1):
            if abs(s-sum(l[i:j+1]))<=min:
                min=abs(s-sum(l[i:j+1]))
                a=sum(l[i:j+1])
    print(a)
