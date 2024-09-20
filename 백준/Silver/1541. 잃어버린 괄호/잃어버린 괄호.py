calc=input().split("-")
calc2=[]
for i in calc:
    a=i.split("+")
    sum=0
    for j in a:
        sum+=int(j)
    calc2.append(sum)
answer=calc2[0]
for i in range(1,len(calc2)):
    answer-=calc2[i]
print(answer)