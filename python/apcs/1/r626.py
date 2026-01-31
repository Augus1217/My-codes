k=int(input())
l=[]
for i in range(k):
    l.append([])
    inpt=input()
    for j in range(0,int(inpt[0])*4,4):
        l[i].append(inpt[j+2:j+5].split())
