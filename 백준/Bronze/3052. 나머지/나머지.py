l=[]
for i in range(10):
    a=int(input())
    l.append(a%42)
l=set(l)
print(len(l))