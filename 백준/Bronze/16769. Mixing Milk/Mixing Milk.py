maximum1, amount1=map(int, input().split())
maximum2, amount2=map(int, input().split())
maximum3, amount3=map(int, input().split())
count=0
while count<=99:
    count+=1
    if count%3==1:
        if maximum2>=amount1+amount2:
            amount2=amount1+amount2
            amount1=0
        if maximum2<amount1+amount2:
            amount1 = amount1 - (maximum2 - amount2)
            amount2=maximum2
    if count % 3 == 2:
        if maximum3>=amount2+amount3:
            amount3=amount2+amount3
            amount2=0
        if maximum3<amount2+amount3:
            amount2 = amount2 - (maximum3 - amount3)
            amount3=maximum3
    if count % 3 == 0:
        if maximum1>=amount1+amount3:
            amount1=amount1+amount3
            amount3=0
        if maximum1<amount1+amount3:
            amount3 = amount3 - (maximum1 - amount1)
            amount1=maximum1
print(amount1)
print(amount2)
print(amount3)