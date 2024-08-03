b1, b2 = input().split()
n1 = int(b1, 2)
n2 = int(b2, 2)
sum1 = n1 + n2
sum2 = bin(sum1)
print(sum2[2:])