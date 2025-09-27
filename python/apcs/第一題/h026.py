f=int(input())
input()
l=[-1]+[int(x) for x in input().split()]
h=[]
k=0
flag=False
for i in l[1:]:
    k+=1
    h.append(f)
    if f==0:
        if i==2:
            print(*h[:k+1],': Won at round',k)
            flag=True
            break
        elif i==5:
            print(*h[:k+1],': Lost at round',k)
            flag=True
            break
    elif f==2:
        if i==5:
            print(*h[:k+1],': Won at round',k)
            flag=True
            break
        elif i==0:
            print(*h[:k+1],': Lost at round',k)
            flag=True
            break
    else:
        if i==0:
            print(*h[:k+1],': Won at round',k)
            flag=True
            break
        elif i==2:
            print(*h[:k+1],': Lost at round',k)
            flag=True
            break
    if l[k]==l[k-1]:
        if i==0:
            f=5
        elif i==2:
            f=0
        else:
            f=2
if flag==False:
    print(*h,': Drew at round',len(h))
