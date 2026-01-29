r,c=map(int,input().split())
l1=[]
l2=[]
for i in range(r):
    l1.append(list(map(int,input().split())))
for i in range(r):
    l2.append(list(map(int,input().split())))
cnt=0
mxcnt=0
for i in range(r):
    for j in range(c):
        if l1[i][j]==l2[i][j]:
            cnt+=1
if mxcnt<cnt:
    mxcnt=cnt
if r==c:
    cnt=0
    for i in range(r):
        for j in range(c):
            if l1[j][i]==l2[i][j]:
                cnt+=1
    if mxcnt<cnt:
        mxcnt=cnt
    cnt=0
    for i in range(r):
        for j in range(c):
            if l1[j][c-1-i]==l2[i][j]:
                cnt+=1
    if mxcnt<cnt:
        mxcnt=cnt
cnt=0
for i in range(r):
    for j in range(c):
        if l1[r-1-i][c-1-j]==l2[i][j]:
            cnt+=1
if mxcnt<cnt:
    mxcnt=cnt
print(f"{int((mxcnt/(r*c))*100)}%")