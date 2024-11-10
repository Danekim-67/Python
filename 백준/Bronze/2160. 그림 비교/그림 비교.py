n=int(input())
l=[]
for i in range(n):
    l2=[]
    for j in range(5):
        l2.append(input())
    l.append(l2)

maxx=-1
x=0
y=0
for i in range(n):
    for j in range(i+1, n):
        count=0
        for k in range(5):
            for m in range(7):
                if l[i][k][m]==l[j][k][m]:
                    count+=1
        if count> maxx:
            maxx=count
            x=i
            y=j

print(x+1, y+1)