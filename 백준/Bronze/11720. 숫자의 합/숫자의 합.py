howmany=int(input())
finallist=[]
calculation=input()
for i in range(howmany):
    finallist.append(int(calculation[i]))
print(sum(finallist))