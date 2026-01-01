m,n=map(int,input().split())
e=[]
for i in range(m):
    e.append([i for i in input()])
t=[i for i in input()]
for i in range(m-1,-1,-1):
    s=""
    for j in range(n-1,-1,-1):
        if e[i][j]=='0':
            s=t[j]+s
        else:
            s=s+t[j]
    if e[i].count("1")%2==1:
        if len(s)%2==1:
            s=s[len(s)//2+1:]+s[len(s)//2]+s[0:len(s)//2]
        else:
            s=s[len(s)//2:]+s[:len(s)//2]
    t=s
print(s)
