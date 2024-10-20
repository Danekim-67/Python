n, k=map(int, input().split())
l=[]
save=[1]*n
for i in range(n):
    l.append(int(input()))
l.sort()
for i in range(n):
    for j in range(i+1, n):
        if (l[j]-l[i])<=k:
            save[i]+=1
print(max(save))