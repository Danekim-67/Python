from itertools import combinations
l=[]
for i in range(9):
    l.append(int(input()))
l.sort()
for i in combinations(l, 7):
    if sum(i)==100:
        for j in range(len(i)):
            print(i[j])
        break