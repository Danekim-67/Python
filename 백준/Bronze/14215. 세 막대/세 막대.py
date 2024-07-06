a, b, c=map(int,input().split())
abc=[]
abc.append(a);abc.append(b);abc.append(c)
maximum=max(abc)
abc.remove(max(abc))
if sum(abc)>maximum:
    print(maximum+sum(abc))
else:
    maximum=sum(abc)-1
    print(maximum+sum(abc))