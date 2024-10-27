n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l2=l[:]
l2.reverse()
left=0
l_count=0
right=0
r_count=0
for i in range(0, len(l)):
    if l[i]>left:
        left=l[i]
        l_count+=1
for i in range(0, len(l2)):
    if l2[i]>right:
        right=l2[i]
        r_count+=1
print(l_count)
print(r_count)