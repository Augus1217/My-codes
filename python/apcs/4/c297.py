l=[]
for i in range(9):
    l.append(input()[2:].split())
n=int(input())
sc=0
out=0
a=b=c=False
i=0
j=0
while out<n:
    if l[i][j]=="1B":
        if c==True:
            sc+=1
            c=False
        if b==True:
            c=True
            b=False
        if a==True:
            b=True
            a=False
        a=True
    elif l[i][j]=="2B":
        if c==True:
            sc+=1
            c=False
        if b==True:
            sc+=1
            b=False
        if a==True:
            c=True
            a=False
        b=True
    elif l[i][j]=="3B":
        if c==True:
            sc+=1
            c=False
        if b==True:
            sc+=1
            b=False
        if a==True:
            sc+=1
            a=False
        c=True
    elif l[i][j]=="HR":
        if c==True:
            sc+=1
            c=False
        if b==True:
            sc+=1
            b=False
        if a==True:
            sc+=1
            a=False
        sc+=1
    elif l[i][j][1]=="O":
        out+=1
        if out%3==0:
            a=False
            b=False
            c=False
    i+=1
    if i==9:
        i=0
        j+=1
print(sc)