alpha=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word=input()
total=0
for i in word:
    for j in alpha:
        if i in j:
            total+=alpha.index(j)+3
print(total)