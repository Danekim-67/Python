n=int(input())
l=[]
for i in range(n):
    a=input()
    s=0
    for j in a:
        if j.isdigit():
            s+=int(j)
    l.append((a,s))
l.sort(key=lambda x: (len(x[0]),x[1],x[0]))
for i in l:
    print(i[0])