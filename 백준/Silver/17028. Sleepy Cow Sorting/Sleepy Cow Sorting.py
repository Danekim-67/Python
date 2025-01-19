n=int(input())
l=list(map(int, input().split()))
cnt=n-1
for i in range(n-2, -1, -1):
    if l[i]>l[i+1]:
        break
    cnt-=1
print(cnt)