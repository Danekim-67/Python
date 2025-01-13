n, m=map(int, input().split())
bessie=[]
for i in range(n):
    a,b =map(int, input().split())
    bessie.append([a, b])
elsie=[]
for i in range(m):
    a,b =map(int, input().split())
    elsie.append([a, b])

bd=[]
for i in range(len(bessie)):
    a=bessie[i][0]
    b=bessie[i][1]

    for j in range(b):
        bd.append(a)
ed=[]
for i in range(len(elsie)):
    a = elsie[i][0]
    b = elsie[i][1]

    for j in range(b):
        ed.append(a)
bt=0
et=0
top=0
beforetop=0
answer=0
for i in range(len(bd)):
    bt+=bd[i]
    et+=ed[i]

    if bt>et:
        top=1
    elif bt<et:
        top=2
    else:
        top=0
    if beforetop>0 and top!=beforetop:
        answer+=1
    beforetop=top
print(answer)