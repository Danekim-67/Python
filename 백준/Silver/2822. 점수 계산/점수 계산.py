l=[]
for i in range(8):
    l.append(int(input()))
a=l[:]
l.sort(reverse=True)
add=[]
for i in range(5):
    add.append(l[i])
print(sum(add))
list=[]
for i in range(5):
    list.append(a.index(add[i])+1)
list.sort()
print(*list)