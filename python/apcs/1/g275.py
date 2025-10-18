for i in range(int(input())):
    a=[bool(int(x)) for x in input().split()]
    b=[bool(int(x)) for x in input().split()]
    s=False
    if (a[1]==a[3]) or (a[1]!=a[5]) or (b[1]==b[3]) or (b[1]!=b[5]):
        print('A',end='')
        s=True
    if (a[6]==False) or (b[6]==True):
        print('B',end='')
        s=True
    if (a[1]==b[1]) or (a[3]==b[3]) or (a[5]==b[5]):
        print('C',end='')
        s=True
    if s==False:
        print('None')
    else:
        print()