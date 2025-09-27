w=0
d={}
for i in range(int(input())):
    t,s=map(int,input().split())
    if s==-1:
        w+=1
    d[t]=s
a=max(d.values())-len(d.values())-w*2
if a<0:
    a=0
for i in d.keys():
    if d[i]==max(d.values()):
        print(a,i)
        break