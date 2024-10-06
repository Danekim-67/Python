a, b=map(int, input().split())
c, d=map(int, input().split())
l=[]
for i in range(a, b):
    l.append(i)
for i in range(c, d):
    l.append(i)
l=set(l)
print(len(l))