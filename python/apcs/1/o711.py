n=int(input())
w1,w2,h1,h2=[int(x) for x in input().split()]
l=[int(x) for x in input().split()]
low=w1*w1*h1
full=low+w2*w2*h2
ct=0
p=0
m=0
for i in range(len(l)):
    ct+=l[i]
    if ct<w1*w1*h1:
        h=ct//(w1*w1)
    elif ct<=w1*w1*h1+w2*w2*h2:
        h=h1+(ct-w1*w1*h1)//(w2*w2)
    else:
        h=h1+h2
    m=max(m,h-p)
    p=h
print(m)

#@title q181. 1. 等紅綠燈
a,b=map(int,input().split())
n=int(input())
l=[int(x) for x in input().split()]
x=0
for i in range(n):
    if l[i]%(a+b)>=a:
        x+=b-(l[i]%(a+b)-a)
print(x)