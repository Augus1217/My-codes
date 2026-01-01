h,w,n=map(int,input().split())
l=[]
board=[[0 for _ in range(w)] for _ in range(h)]
for i in range(n):
    l.append([int(x) for x in input().split()])
for i in l:
    for j in range(i[0]-i[2],i[0]+i[2]+1):
        for k in range(i[1]-i[2],i[1]+i[2]+1):
            if abs(i[1]-k)+abs(i[0]-j)<=i[2] and 0<=j<h and 0<=k<w:
                board[j][k]+=i[3]
for i in board:
    print(*i)
