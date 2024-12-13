n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

height=l[:]
cows=sorted(l)
count=0

change=[0]*n
for i in range(n):
    if l[i]==cows[i]:
        continue
    else:
        count+=1
if count==0:
    print(0)
else:
    print(count-1)