a,b=map(int,input().split())
c=0
for i in range(int(input())):
    l=[int(x) for x in input().split()][:-1]
    ca=cb=0
    for i in l:
        if i==a:
            ca+=1
        elif i==b:
            cb+=1
        elif i==-a:
            ca-=1
        elif i==-b:
            cb-=1
    if ca>0 and cb>0:
        c+=1
print(c)