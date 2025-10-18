n,m,k=map(int, input().split())
a_l=[int(x) for x in input().split()]
b_l=[int(x) for x in input().split()]
sym=[]
outlist=[[0]*n]*m
for i in range(n):
    sym.append([x for x in input().split()])
for i in range(n):
    for j in range(m):
        if i==0:
            a=a_l[0]
        else:
            a=outlist[i]-1
        if j==0:
            b=b_l[0]
        else:
            b=outlist[i]-1