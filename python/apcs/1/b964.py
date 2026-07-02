n=int(input())
l=sorted([int(x) for x in input().split()])
high="worst case"
low="best case"
for i in range(n):
    if l[i]>=60:
        high=l[i]
        break
    elif l[i]<60:
        low=l[i]
print(*l)
print(low,high,sep="\n")