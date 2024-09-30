n=input()
l=[]
for i in range(len(n)):
    l.append(n[i])
l.sort(reverse=True)
for i in range(len(n)):
    print(l[i], end="")