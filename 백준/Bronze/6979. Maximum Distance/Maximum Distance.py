n=int(input())
for i in range(n):
    long=int(input())
    l1=list(map(int, input().split()))
    l2=list(map(int, input().split()))
    l=[]
    for j in range(long):
        for k in range(j, long):
            if l1[j]==l2[k]:
                l.append(j-k)
    if l:
        print("The maximum distance is", abs(min(l)))
        print()
    else:
        print("The maximum distance is 0")
        print()