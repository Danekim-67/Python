n,k=map(int, input().split())
l=list(map(int, input().split()))
l.sort()
count=k+1
for i in range(len(l)-1):
    if l[i+1]-l[i]<=k:
        count+=l[i+1]-l[i]
    else:
        count+=k+1
print(count)