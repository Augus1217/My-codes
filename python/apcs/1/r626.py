k=int(input())
l=[]
for i in range(k):
    a=input().split()
    l.append([])
    for j in range(1, int(a[0])*2+1, 2):
        l[i].append([a[j], a[j+1]])
while True:
    
print(l)        