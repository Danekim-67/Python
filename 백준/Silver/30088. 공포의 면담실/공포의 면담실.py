n=int(input())
wow=0
l1=[]
for i in range(n):
    l=list(map(int, input().split()))
    l1.append(sum(l[1:]))
    add=0
    add1=0
    l1.sort()
for j in range(len(l1)):
     add1 += add
     add+=l1[j]
wow+=add+add1
print(wow)