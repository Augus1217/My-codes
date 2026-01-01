from collections import Counter
m,n,k=map(int, input().split())
l=[]
mo=[]
s=0
for i in range(m):
    l.append(list(input()))
for i in range(k):
    mo.append([int(x) for x in input().split()])
for i in range(k):#First move
    for j in range(m):#First Circle
        for o in range(n):#First text
            if o!=0:
                l[j]=l[j][mo[i][j]%n:]+l[j][:mo[i][j]%n]
    #print(l)
    for j in range(n):
        c=[]
        for o in range(m):
            c.append(l[o][j])
        s+=Counter(c).most_common(1)[0][1]
print(s)
