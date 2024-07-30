l = [ ]
for i in range (int(input())):
    l.append(input())
#n=int(input()); l=[input() for i in range(n)]
l2=list(set(l))
l2.sort()
l2.sort(key=len)

for i in l2:
    print(i)