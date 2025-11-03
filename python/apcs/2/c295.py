l=[]
n,m=map(int,input().split())
for i in range(n):
    l.append(max([int(x) for x in input().split()]))
x=sum(l)
p=[]
for i in l:
    if x%i==0:
        p.append(i)
print(x)
if p==[]:
    print(-1)
else:
    print(*p)