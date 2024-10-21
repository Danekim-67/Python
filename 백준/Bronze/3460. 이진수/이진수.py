repeat=int(input())
for i in range(repeat):
    n=int(input())
    list=[]
    while n!=0:
        list.append(n%2)
        n=n//2
    for i in range(len(list)):
        if list[i]==1:
            print(i, end=" ")