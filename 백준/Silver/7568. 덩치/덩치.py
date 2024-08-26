l=[]
rank=[]
for i in range(int(input())):
    x, y=map(int, input().split())
    l.append([x, y])
    rank.append(1)

for i in range(len(l)):
    for j in range(len(l)):
        if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
            rank[i]+=1
for i in range(len(rank)):
    print(rank[i], end=" ")