a, b, c, m=map(int,input().split())
t=0
w=0
if a <= m:
    for i in range(24):
        if t + a<=m:
            t=t+a
            w+=b
        else:
            t-=c
            if t<0:
                t=0
print(w)