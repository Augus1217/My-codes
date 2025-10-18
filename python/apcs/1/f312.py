a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
n=int(input())
l=[]
for x1 in range(n+1):
    y1=a1*pow(x1,2)+b1*x1+c1
    y2=a2*pow(n-x1,2)+b2*(n-x1)+c2
    l.append(y1+y2)
print(max(l))