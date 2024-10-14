n=int(input())
change=list(map(int, input().split()))
dance=list(map(int, input().split()))
for i in range(n):
    change[i]=change[i]-1
for i in range(3):
    l1 = dance[:]
    for j in range(n):
        dance[j]=l1[change[j]]
for i in range(n):
    print(dance[i])