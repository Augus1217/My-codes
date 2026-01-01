n,m,k=map(int,input().split())
l=[[int(i) for i in input().split()] for _ in range(k)]
board=set()
d2=[]
alive=k
while alive>0:
    d1=set()
    for i in range(len(l)):
        if i in d2:
            continue
        board.add(tuple([l[i][0],l[i][1]]))
    for i in range(len(l)):
        if i in d2:
            continue
        l[i][0]+=l[i][2]
        l[i][1]+=l[i][3]
        if not(0<=l[i][0]<n) or not(0<=l[i][1]<m):
            d2.append(i)
            alive-=1
        elif tuple([l[i][0],l[i][1]]) in board:
            d1.add(tuple([l[i][0],l[i][1]]))
            d2.append(i)
            alive-=1
    for j in d1:
        board.remove(j)
print(len(board))
