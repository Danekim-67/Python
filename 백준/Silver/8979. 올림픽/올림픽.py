n, k=map(int, input().split())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
a=0
for i in range(n):
    if l[i][0]==k:
        a=i
for i in range(n):
    if l[a][1:]==l[i][1:]:
        print(i+1)
        break