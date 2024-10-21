n,length=map(int,input().split())
l=list(map(int, input().split()))
l.sort()
for i in range(len(l)):
    if length>=l[i]:
        length+=1
print(length)