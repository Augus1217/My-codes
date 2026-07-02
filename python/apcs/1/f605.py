x,cost=0,0
n,d=map(int,input().split())
for i in range(n):
    a,b,c=map(int,input().split())
    if max(a,b,c)-min(a,b,c)>=d:
        x+=1
        cost+=sum([a,b,c])//3
print(x,cost)