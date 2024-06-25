howmany=int(input())
for i in range(howmany):
    repeat, word = (input().split())
    repeat = int(repeat)
    for j in range(len(word)):
        print(word[j]*repeat,end="")
    print()