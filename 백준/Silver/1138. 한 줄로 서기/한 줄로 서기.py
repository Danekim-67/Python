n = int(input())
h = list(map(int, input().split()))
r = []
j=-1
h2=[]
for i in range(1, n+1):
    h2.append(i)

for i in range(1, n + 1):
    p = h[j]
    r.insert(p, h2[j])
    j=j-1
print(*r)