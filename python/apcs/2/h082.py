n,m=map(int,input().split())
s=[0]+[int(x) for x in input().split()]
t=[0]+[int(x) for x in input().split()]
idx=[int(x) for x in input().split()]
fail=[0]*(n+1)
while len(idx)>1:
    win=[]
    lose=[]
    for i in range(0,len(idx)-1,2):
        a,b,c,d=s[idx[i]],t[idx[i]],s[idx[i+1]],t[idx[i+1]]
        if a*b>=c*d:
            s[idx[i]]=a+c*d//(2*b)
            t[idx[i]]=b+c*d//(2*a)
            s[idx[i+1]]=c+c//2
            t[idx[i+1]]=d+d//2
            fail[idx[i+1]]+=1
            if fail[idx[i]]<m:
                win.append(idx[i])
            if fail[idx[i+1]]<m:
                lose.append(idx[i+1])
        else:
            s[idx[i+1]]=c+a*b//(2*d)
            t[idx[i+1]]=d+a*b//(2*c)
            s[idx[i]]=a+a//2
            t[idx[i]]=b+b//2
            fail[idx[i]]+=1
            if fail[idx[i+1]]<m:
                win.append(idx[i+1])
            if fail[idx[i]]<m:
                lose.append(idx[i])
    if len(idx)%2==1:
        win.append(idx[-1])
    idx=win+lose
print(idx[0])
