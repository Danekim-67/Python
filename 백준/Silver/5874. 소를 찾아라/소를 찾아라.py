s = input()
n = len(s)
bl = []
fl= []
for i in range(n - 1):
    if s[i:i + 2] == '((':
        bl.append(i)
    elif s[i:i + 2] == '))':
        fl.append(i)
count = 0
front = 0
num = len(fl)
for back in bl:
    while front < num and fl[front] <= back:
        front += 1
    count += num - front
print(count)