l=[]
for i in range(5):
    l.append(int(input()))
l.sort()
print(sum(l)//5)
print(l[2])