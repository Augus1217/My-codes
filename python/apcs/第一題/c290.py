l=[int(x) for x in input()]
odd=sum([l[i] for i in range(1,len(l),2)])
even=sum([l[i] for i in range(0,len(l),2)])
print(abs(odd-even))