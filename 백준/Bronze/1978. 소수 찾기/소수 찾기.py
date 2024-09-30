n=int(input())
l=list(map(int, input().split()))
howmany=0
for i in range(n):
    if l[i] == 1:
        continue
    for j in range(2,l[i]):
        if l[i]%j==0:
            break
    else:
        howmany+=1
print(howmany)