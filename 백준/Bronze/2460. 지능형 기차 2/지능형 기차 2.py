people=0
l=[]
for i in range(10):
    out, come=map(int, input().split())
    people=people-out
    people=people+come
    l.append(people)
print(max(l))