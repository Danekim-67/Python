ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for i in ca:
    word = word.replace(i, '.')
print(len(word))