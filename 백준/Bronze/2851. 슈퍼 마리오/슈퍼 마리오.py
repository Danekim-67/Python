l=[]
for i in range (10):
    l.append(int(input()))
addition1=0
addition2=0
for i in range (10):
    addition1+=l[i]
    if i==0:
        continue
    else:
        addition2+=l[i-1]
    if addition1>=100:
        if abs(100-addition1)>abs(100-addition2):
            print(addition2)
            break
        else:
            print(addition1)
            break
if addition1<100:
    print(addition1)