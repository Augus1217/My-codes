n=input()
o=sum([int(x) for x in n[::2]])
e=sum([int(x) for x in n[1::2]])
print(abs(o-e))