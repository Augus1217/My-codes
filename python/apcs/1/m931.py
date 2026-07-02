n=int(input())
l={}
for i in range(n):
    a,d=map(int,input().split())
    l[(pow(a,2)+pow(d,2))]=f'{a} {d}'
del l[max(l.keys())]
print(l[max(l.keys())])

#@title o076. 1. 特技表演
a=int(input())
l=[int(x) for x in input().split()]
max=0
for i in range(a):
    c=1
    for j in range(i,a-1):
        if l[j]>l[j+1]:
            c+=1
        else:
            break
    if c>max:
        max=c
print(max)