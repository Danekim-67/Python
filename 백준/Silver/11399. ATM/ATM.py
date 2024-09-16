n=int(input())
l=list(map(int, input().split()))
add=0
add1=0
l.sort()
for i in range(n):
    add1 += add
    add+=l[i]
print(add+add1)