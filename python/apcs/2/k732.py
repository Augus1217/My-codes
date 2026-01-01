n,m=map(int,input().split())
a=[[int(x) for x in input().split()] for _ in range(n)]
p=[]
for i in range(n):
    for j in range(m):
        count=0
        for k in range(i-a[i][j],i+a[i][j]+1):
            for l in range(j-a[i][j],j+a[i][j]+1):
                if 0<=k<n and 0<=l<m:
                    if abs(i-k)+abs(j-l)<=a[i][j]:
                        count+=a[k][l]
        if count%10==a[i][j]:
            p.append(f'{i} {j}')
print(len(p),*p,sep='\n')
