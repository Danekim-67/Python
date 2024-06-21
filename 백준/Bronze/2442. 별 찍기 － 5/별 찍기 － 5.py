howmany=int(input())
for i in range(1, howmany+1):
    print(' '*(howmany-1)+"*"*((2*i)-1))
    howmany -=1