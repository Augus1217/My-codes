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
