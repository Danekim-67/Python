n=int(input())
l=[]
area=0
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        for k in range(n):
            point1=l[i]
            point2=l[j]
            point3=l[k]
            if point1[0]==point2[0]==point3[0] or point1[1]==point2[1]==point3[1]:
                pass
            if point1[1]==point2[1] and point1[0]==point3[0]:
                if area<abs(point1[0]-point2[0])*abs(point1[1]-point3[1]):
                    area=abs(point1[0]-point2[0])*abs(point1[1]-point3[1])
print(area)
