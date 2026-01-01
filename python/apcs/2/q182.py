a=list(input())
t=''
for j in range(int(input())):
    x=int(input())
    l=[]
    if x==0:
        for i in range(0,len(a),2):
            t=a[i+1]
            a[i+1]=a[i]
            a[i]=t
    elif x==1:
        for i in range(0,len(a),2):
            l.append(a[i])
            l.append(a[i+1])
            l[i:i+2]=sorted(l[i:i+2])
        a=l.copy()
    else:
        l.append(a[:len(a)//2])
        l.append(a[len(a)//2:])
        for i in range(0,len(a),2):
            a[i]=l[0][i//2]
            a[i+1]=l[1][i//2]
print(''.join(a))
