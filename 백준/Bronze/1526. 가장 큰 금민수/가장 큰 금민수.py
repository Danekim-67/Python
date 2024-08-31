n=int(input())
for i in range(n,3,-1):
    if "1" in str(i) or "2" in str(i) or "3" in str(i) or "5" in str(i) or "6" in str(i) or "8" in str(i) or "9" in str(i) or "0" in str(i):
        continue
    else:
        print(i)
        break