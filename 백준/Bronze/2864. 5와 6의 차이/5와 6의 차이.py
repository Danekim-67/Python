a, b=input().split()
a1=a; b1=b
a2=a; b2=b
a1=a1.replace("5", "6")
b1=b1.replace("5", "6")
a2=a2.replace("6", "5")
b2=b2.replace("6", "5")
print(int(a2)+int(b2),int(a1)+int(b1))