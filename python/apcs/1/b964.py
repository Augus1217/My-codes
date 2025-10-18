n=int(input())
l=sorted([int(x) for x in input().split()])
print(*l)
if min(l)>=60:
    print('best case')
else:
    for i in range(len(l)-1,-1,-1):
        if l[i]<60:
            print(l[i])
            break
if max(l)<60:
    print('worst case')
else:
    for i in range(len(l)):
        if l[i]>=60:
            print(l[i])
            break
