s,t,n,m,r=map(int,input().split())

sl=[[int(x) for x in input().split()] for _ in range(s)]
ll=[[int(x) for x in input().split()] for _ in range(n)]
ok_l=0
num=[]
for i in range(n-s+1):
    for j in range(m-t+1):
        n=0
        for k in range(s):
            for l in range(t):
                if sl[k][l]!=ll[i+k][j+l]:
                    n+=1
        if n<=r:
            ok_l+=1
            num.append([ll[i+x][j:j+t] for x in range(s)])
min=99999
sum_sl=sum([sum(sl[x]) for x in range(s)])
sum_num=[]
for i in range(ok_l):
    n=0
    for j in range(s):
        n+=sum(num[i][j])
    sum_num.append(n)
for i in sum_num:
    if abs(sum_sl-i)<min:
        min=abs(sum_sl-i)
if min==99999:
    print(-1)
else:
    print(min)
