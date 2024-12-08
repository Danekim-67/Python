l=[]
inl=[]
green=0
yellow=0
for j in range(3):
    l.append(list(input()))
for i in range(3):
    inl.append(list(input()))
for i in range(3):
    for j in range(3):
        if inl[i][j]==l[i][j]:
            green+=1
            l[i][j] = "!"
            inl[i][j] = "."
for i in range(3) :
    for j in range(3) :
        for k in range(3) :
            if inl[i][j] in l[k] :
                q = l[k].index(inl[i][j])
                l[k][q] = "?"
                yellow += 1
                break
print(green)
print(yellow)