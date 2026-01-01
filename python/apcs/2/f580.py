n,m=map(int,input().split())
l=[[1,2,6,5,4,3] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    if a>0 and b>0:
        l[a-1],l[b-1]=l[b-1],l[a-1]
    elif b==-1:
        l[a-1][0],l[a-1][5],l[a-1][2],l[a-1][4]=l[a-1][5],l[a-1][2],l[a-1][4],l[a-1][0]
    else:
        l[a-1][0],l[a-1][3],l[a-1][2],l[a-1][1]=l[a-1][3],l[a-1][2],l[a-1][1],l[a-1][0]
for i in l:
    print(i[0],end=' ')
