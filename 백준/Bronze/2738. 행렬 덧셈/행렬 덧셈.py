a=[]
b=[]
c=[]
space=0
x, y=map(int, input().split())

for i in range(x):
    r=list(map(int, input().split()))
    a.append(r)
for i in range(x):
    r=list(map(int, input().split()))
    b.append(r)
for i in range (x):
    for j in range (y):
       c.append((a[i][j])+(b[i][j]))
for i in range(y):
    for j in range(x):
        space+=1
        if space!=x:
            print(c[j+(x*i)], end=" ")
        else:
            print(c[j+(x*i)])
            space=0