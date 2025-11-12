a=[2,5]
b=[1,3]
c=[1,1]
for i in range(1,32):
    count=0
    if i%(a[0]+a[1])<a[0]:
        count+=1
    if i%(b[0]+b[1])<b[0]:
        count+=1
    if i%(c[0]+c[1])<c[0]:
        count+=1
    if count==3:
        print("9/"+str(i))