from itertools import permutations
n=int(input())
l=[]
for i in range(n):
    limit=input().split()
    l.append([limit[0], limit[-1]])
cows=["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
cows.sort()
pl=list(permutations(cows, 8))
for i in pl:
    flag = True
    for j in range(n):
        if abs(i.index(l[j][0])-i.index(l[j][1]))==1:
            pass
        else:
            flag=False
    if flag==True:
        for k in range(len(cows)):
            print(*i, sep="\n")
            exit()
