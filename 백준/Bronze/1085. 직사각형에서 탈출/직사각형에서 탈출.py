x, y, w, h=map(int, input().split())
a=[];a.append(w-x);a.append(x);a.append(y);a.append(h-y)
print(min(a))