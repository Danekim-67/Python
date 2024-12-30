n = int(input())
l = []
cow = [7, 7, 7] # Bessie, Elsie, Mildred
for i in range(n) :
    l.append(input().split())

for i in range(n) :
    l[i][0] = int(l[i][0])
l.sort()
new = []
cnt = 0
for i in range(n):
    if l[i][1] == "Bessie":
        cow[0]=cow[0]+int(l[i][2])
    elif l[i][1] == "Elsie":
        cow[1]=cow[1]+int(l[i][2])
    elif l[i][1] == "Mildred" :
        cow[2]=cow[2]+int(l[i][2])
    check = []
    if cow[0] == max(cow) :
        check.append("Bessie")
    if cow[1] == max(cow) :
        check.append("Elsie")
    if cow[2] == max(cow) :
        check.append("Mildred")
    if check != new :
        cnt += 1
    new = check
print(cnt)
