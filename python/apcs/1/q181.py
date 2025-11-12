a,b=map(int,input().split())
n=int(input())
l=[int(x) for x in input().split()]
x=0
for i in range(n):
    if l[i]%(a+b)>=a:
        x+=b-(l[i]%(a+b)-a)
print(x)