l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
start=1000
reading=[]
for i in range(10):
    for j in range(11):
        for k in range(10):
            for m in range(11):
                l1c=l1.copy()
                l2c=l2.copy()
                milk1=start
                milk2=start

                b1=l1c[i]
                milk1-=b1
                milk2+=b1
                l2c.append(b1)
                l1c.pop(i)

                b2=l2c[j]
                milk1+=b2
                milk2-=b2
                l1c.append(b2)
                l2c.pop(j)

                b3=l1c[k]
                milk1-=b3
                milk2+=b3
                l2c.append(b3)
                l1c.pop(k)

                b4=l2c[m]
                milk1+=b4
                milk2-=b4
                l1c.append(b4)
                l2c.pop(m)

                reading.append(milk1)

reading=set(reading)
print(len(reading))