a,b,c=sorted([int(x) for x in input().split()])
print(a,b,c)
if a+b>c:
    if a**2+b**2<c**2:
        print('Obtuse')
    elif a**2+b**2==c**2:
        print('Right')
    elif a**2+b**2>c**2:
        print('Acute')
else:
    print('No')