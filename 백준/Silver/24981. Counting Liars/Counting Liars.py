n=int(input())
l=[]
for i in range(n):
    t, v=input().split()
    l.append((t, int(v)))

l2=[]
for i in range(len(l)):
    loc=l[i][1]
    liar=0
    for j in range(len(l)):
        if l[j][0]=="G":
            if loc<l[j][1]:
                liar+=1
        if l[j][0]=="L":
            if loc>l[j][1]:
                liar+=1
    l2.append(liar)
print(min(l2))