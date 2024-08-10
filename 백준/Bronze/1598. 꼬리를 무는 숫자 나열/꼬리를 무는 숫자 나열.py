a, b= map(int,input().split())
row=abs(((b-1)//4+1)-((a-1)//4+1))
col=abs(((b-1)%4)-((a-1)%4))
print(row+col)