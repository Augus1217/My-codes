import copy
r,c,m=map(int,input().split())
l=[[int(x) for x in input().split()] for i in range(r)]
o=[int(x) for x in input().split()]
for i in range(m-1,-1,-1):
    if o[i]==0:
        r,c=c,r
        l2=[[0 for _ in range(c)] for _ in range(r)]
        for j in range(c):
            for k in range(r):
                l2[r-k-1][j]=l[j][k]
    else:
        l2=[[0 for _ in range(c)] for _ in range(r)]
        for j in range(r):
            l2[j]=l[r-j-1]
    l=l2.copy()
print(r,c)
for i in l:
    print(*i)
