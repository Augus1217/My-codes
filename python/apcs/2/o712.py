#@title o712. 2. 蒐集寶石
m,n,k,r,c = [int(x) for x in input().split()]
b=[]
for i in range(m):
    b.append([int(x) for x in input().split()]+[-1])
b.append([-1]*n)
d=0 #方向
c=0 #寶石數
score=0
dr=(0,1,0,-1)
dc=(1,0,-1,0)
while b[r][c]:
    c+=1
    score+=b[r][c]
    b[r][c]-=1
    if score%k==0:
        d=(d+1)%4
    while True:
        nr=r+dr[d];nc=c+dc[d]
        if b[nr][nc]>=0:
            r,c=nr,nc
            break
        d=(d+1)%4
        print(d)
print(c)