n=int(input())
l=[]
for i in range(n):
    a=list(input().split())
    char=a[2:]
    l.append(char)
yes=0
yesl=[]
for i in range(n):
    for j in range(i+1, n):
        yes=0
        for k in range(0, len(l[i])):
            for m in range(0, len(l[j])):
                if l[i][k]==l[j][m]:
                    yes+=1
        yesl.append(yes)
print(max(yesl)+1)