n=int(input())
list=[]
while n!=0:
    list.append(n%2)
    n=n//2
list.reverse()
for i in range(len(list)):
    print(list[i], end="")