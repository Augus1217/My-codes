l=[0 for _ in range(50)]
for i in range(50):
    for j in range(-1,50,i+1):
        l[j]+=1
for i in range(50):
    if l[i]%2==1:
        print(i+1)