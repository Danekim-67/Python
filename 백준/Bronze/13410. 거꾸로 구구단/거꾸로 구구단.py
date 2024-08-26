n, k=map(int, input().split())
l=[]
l2=[]
for i in range(1, k+1):
        l.append(n*i)
for i in range(len(l)):
    l[i]=str(l[i])
    l2.append(l[i][::-1])
    l2[i]=int(l2[i])
print(max(l2))