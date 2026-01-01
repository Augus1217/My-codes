l=[int(x) for x in input().split()]
if sorted(l)==sorted(list(set(l))):
    print(1,*sorted(l,reverse=True))
elif len(set(l))==1:
    print(3,l[0])
else:
    print(2,*sorted(set(l),reverse=True))
