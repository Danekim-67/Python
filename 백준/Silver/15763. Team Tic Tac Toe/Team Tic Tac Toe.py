l=[]
for i in range(3):
    l.append(list(input()))

l2=[[l[0][0],l[1][0],l[2][0]],[l[0][1],l[1][1],l[2][1]],[l[0][2],l[1][2],l[2][2]],[l[0][0],l[1][1],l[2][2]],[l[0][2],l[1][1],l[2][0]]]
win1=[]
win2=[]
for i in range(3):
    if len(set(l[i]))==1:
        win1.append(l[i][0])
    elif len(set(l[i]))==2:
        win2.append(l[i])
for i in range(5):
    if len(set(l2[i]))==1:
        win1.append(l2[i][0])
    elif len(set(l2[i]))==2:
        win2.append(l2[i])
print(len(list(set(win1))))
for i in range(len(win2)):
    listlength=len(win2)
    win2[i]=set(win2[i])

win2 = list(win2)
win2.sort()
win2=[list(item) for item in set(tuple(i) for i in win2)]
print(len(win2))
save=0
for i in win2:
    if win2.index(i)==1:
        save=i
    else:
        if i==save:
            win2.remove(i)

