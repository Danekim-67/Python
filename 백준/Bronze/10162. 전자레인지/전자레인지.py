time=int(input())
a=300; b=60; c=10
if time%10!=0:
    print("-1")
else:
    print(time//a,(time%a)//b,((time%a)%b)//c)