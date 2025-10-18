a,d=map(int,input().split())
n=0
l=[int(x) for x in input().split()]
m=0
a=l.pop(0)
for i in l:
    if a!=None and i>=a+d:
        m+=i-a
        n=i
        a=None
    elif a==None:
        if n-i>=d:
            a=i
print(m)