n,k,m=map(int, input().split())
c=0
l=[int(x) for x in input().split()]
for i in range(n-k+1):
    if sum(l[i:i+k])/k>=m:
        c+=1
print(c)