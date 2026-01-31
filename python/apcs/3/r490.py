n=int(input())
l=[]
for i in range(n):
    l.append(input())
dic={}
for i in l:
    sodd=sum(list(map(int,i[:12:2])))
    seven=sum(list(map(int,i[1:12:2])))
    c=int(i[12])
    if (sodd+3*seven)%10+c==0 or (sodd+3*seven)%10+c==10:
        if i[:3] not in dic:
            dic[i[:3]]=1
        else:
            dic[i[:3]]+=1
y=max(dic.values())
for a,b in dic.items():
    if b==y:
        print(a,b)
        break