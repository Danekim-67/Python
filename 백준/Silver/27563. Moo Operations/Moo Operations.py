n=int(input())
for i in range(n):
    word=input()
    length=len(word)

    if "MOO" in word:
        print(length-3)
    elif "OOO" in word:
        print(length-2)
    elif "MOM" in word:
        print(length-2)
    elif "OOM" in word:
        print(length-1)
    else:
        print(-1)
