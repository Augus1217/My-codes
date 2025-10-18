x,n=map(int,input().split())
l=[int(x) for x in input().split()]
e=[]
w=[]
for i in l:
    if i<x:
        e.append(i)
    else:
        w.append(i)
if len(e)>len(w):
    print(len(e),min(e))
else:
    print(len(w),max(w))