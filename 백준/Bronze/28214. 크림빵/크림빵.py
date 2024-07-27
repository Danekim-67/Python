N, K, P=map(int, input().split())
a=list(map(int, input().split()))
total=0
for i in range(N):
    add=0
    for j in range(K):
        add+=a[i*K+j]
    if add>K-P:
        total+=1
    else:
        continue
print(total)