l=[]
for i in range(int(input())):
    l.append([int(x) for x in input().split()])
for i in range(len(l)-1):
    l[i]=abs(l[i][0]-l[i+1][0])+abs(l[i][1]-l[i+1][1])
del l[-1]
print(max(l),min(l))