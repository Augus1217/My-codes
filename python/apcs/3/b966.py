n=int(input())
l=[]
for i in range(n):
    l.append([int(x) for x in input().split()])
l=sorted(l)
a,b,t=0,0,0
for [x1,x2] in l:
    if x1<=b:
        b=max(x2,b)
    else:
        t+=b-a
        a,b=x1,x2
t+=b-a
print(t)
