n=int(input())
cows=["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
count1=[0]*7
l=[]
for i in range(n):
    l.append(list(input().split()))
for i in range(n):
    l[i][1]=int(l[i][1])
for i in range(n):
    if l[i][0]=="Bessie":
        count1[0]+=l[i][1]
    elif l[i][0]=="Elsie":
        count1[1]+=l[i][1]
    elif l[i][0]=="Daisy":
        count1[2]+=l[i][1]
    elif l[i][0]=="Gertie":
        count1[3]+=l[i][1]
    elif l[i][0]=="Annabelle":
        count1[4]+=l[i][1]
    elif l[i][0]=="Maggie":
        count1[5]+=l[i][1]
    elif l[i][0]=="Henrietta":
        count1[6]+=l[i][1]
countl2=[]
for i in count1:
    if i in countl2:
        continue
    else:
        countl2.append(i)
check = 0
c = [0] * 7
if len(countl2)>=2:
    countl2.sort()
    k=countl2[1]
    for i in count1:
        if i == k:
            check += 1
            c[count1.index(i)] = 1
    if check == 1:
        print(cows[c.index(1)])
    else:
        print("Tie")
else:
    print("Tie")
    exit()



