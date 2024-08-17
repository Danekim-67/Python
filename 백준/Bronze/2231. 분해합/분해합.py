n=int(input())
check=0
for i in range (n):
    if i+sum(map(int,str(i)))==n:
        print(i)
        check=1
        break
if check==0:
    print("0")