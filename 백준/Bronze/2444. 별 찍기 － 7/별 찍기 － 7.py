howmany=int(input())
howmany2=howmany
for i in range(1, howmany):
    print(' '*(howmany-1)+"*"*((2*i)-1))
    howmany -=1
print("*"*(howmany2*2-1))
howmany2-=1
for i in range(1, howmany2+1):
    print(" "*i+"*"*((2*howmany2)-1))
    howmany2-=1