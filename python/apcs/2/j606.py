k,q,r=map(int,input().split())
s=[i for i in input()]
news=['_' for _ in range(k)]
l=[]
t=[]
for i in range(q):
    l.append([int(x) for x in input().split()])
for i in l:
    for j in range(k):
        news[i[j]-1]=s[j]
    t.append(news)
    s=news
    news=['_' for _ in range(k)]

for i in range(r):
    for j in range(q):
        print(t[j][i],end='')
    print()
