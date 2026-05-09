n=int(input())
s=input()
l=[]
cnt=1
for i in range(len(s)):
    if s[i].isupper():
        l.append(1)
    else:
        l.append(0)
    print(i)
a=[]
for i in range(len(s)-1):
    if l[i]==l[i+1]:
        cnt+=1
    else:
        a.append(cnt)
        cnt=1
a.append(cnt)
print(l,a)