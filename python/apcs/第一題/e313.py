d={}
d2={}
s=int(input())
for i in range(s):
    t=input()
    d[t]=len(set(t))
n=min(list(d.values()))
for k,v in d.items():
    if v==n:
        d2[k]=v
d={}
for i in sorted(d2):
    d[i]=d2[i]
print(list(d.keys())[0])