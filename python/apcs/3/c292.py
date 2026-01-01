n=int(input())
a=int(input())
l=[[int(i) for i in input().split()] for i in range(n)]
now=[n//2,n//2]
print(l[now[0]][now[1]],end='')
for i in range(1,n//2+1):
    if a==0:
        now[1]-=1
        print(l[now[0]][now[1]],end='')
        for j in range(1,i*8):
            if j//(i*2)==0:
                now[0]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==1:
                now[1]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==2:
                now[0]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==3:
                now[1]-=1
                print(l[now[0]][now[1]],end='')
    elif a==1:
        now[0]-=1
        print(l[now[0]][now[1]],end='')
        for j in range(1,i*8):
            if j//(i*2)==0:
                now[1]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==1:
                now[0]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==2:
                now[1]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==3:
                now[0]-=1
                print(l[now[0]][now[1]],end='')

    elif a==2:
        now[1]+=1
        print(l[now[0]][now[1]],end='')
        for j in range(1,i*8):
            if j//(i*2)==0:
                now[0]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==1:
                now[1]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==2:
                now[0]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==3:
                now[1]+=1
                print(l[now[0]][now[1]],end='')
    elif a==3:
        now[0]+=1
        print(l[now[0]][now[1]],end='')
        for j in range(1,i*8):
            if j//(i*2)==0:
                now[1]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==1:
                now[0]-=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==2:
                now[1]+=1
                print(l[now[0]][now[1]],end='')
            elif j//(i*2)==3:
                now[0]+=1
                print(l[now[0]][now[1]],end='')
print('\n')
