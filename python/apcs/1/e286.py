t1=sum([int(x) for x in input().split()])
p1=sum([int(x) for x in input().split()])
t2=sum([int(x) for x in input().split()])
p2=sum([int(x) for x in input().split()])
print(f'{t1}:{p1}')
print(f'{t2}:{p2}')
if t1>p1 and t2>p2:
    print('Win')
elif t1<p1 and t2<p2:
    print('Lose')
else:
    print('Tie')