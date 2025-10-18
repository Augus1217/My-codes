a=int(input())
c=0
l=[int(x) for x in input().split()]
if l[0]==0:
    c+=l[1]
if l[-1]==0:
    c+=l[-2]
for i in range(1,len(l)-1):
    if l[i]==0:
        c+=min(l[i-1],l[i+1])
print(c)