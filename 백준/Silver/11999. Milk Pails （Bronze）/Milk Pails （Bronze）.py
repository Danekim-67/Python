x, y, m=map(int, input().split())
l=[]
for i in range(m, 0, -1):
    for j in range((m//y)+1):
        for k in range((m//x)+1):
            if i==(j*y)+(k*x):
                l.append(i)
print(max(l))