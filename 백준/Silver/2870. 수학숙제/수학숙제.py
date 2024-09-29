n=int(input())
l=[]
num=["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(n):
    l.append(input())
answer=[]
s=''
for i in range(n):
    for j in l[i]:
        if j in num:
            s+=j
        else:
            if s:
                answer.append(s)
                s=''
    if s:
        answer.append(s)
        s=''
answer2=[]
for i in answer:
   answer2.append(int(i))
answer2.sort()
for i in range(len(answer2)):
    print(answer2[i])