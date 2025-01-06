n= int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(n):
    for j in range(3):
        print(l[i][j], end=" ")
    print()