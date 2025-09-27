x=False
a,b,c=map(bool,map(int,input().split()))
if (a and b)==c:
    print('AND')
    x=True
if (a or b)==c:
    print('OR')
    x=True
if (a ^ b)==c:
    print('XOR')
    x=True
if x==False:
    print('IMPOSSIBLE')