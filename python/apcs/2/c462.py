k=int(input())
s=input()
now=""
s01=""
last=None
for i in s:
    if i.islower():
        if last!="low":
            s01+="1"
        else:
            s01=s01[:-1]+str(int(s01[-1])+1)
        last="low"
    else:
        if last!="up":
            s01+="1"
        else:
            s01=s01[:-1]+str(int(s01[-1])+1)
        last="up"
sk=""
for i in s01:
    if int(i)==k:
        sk+="1"
    elif int(i)>k:
        sk+="2"
    else:
        sk+="0"
maxgo=0
go=0
locate=0
for i in range(len(sk)):
    if sk[i]=="1":
        go+=1
        if go>maxgo:
            maxgo=go
            locate=i
    else:
        go=0
add=0
if locate+1!=len(sk):
    if sk[locate+1]=="2":
        add+=1
if locate+1-maxgo>0:
    if sk[locate-maxgo]=="2":
        add+=1
print((maxgo+add)*k)