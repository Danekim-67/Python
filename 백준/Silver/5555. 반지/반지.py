what=input()
repeat=int(input())
howmany=0
for i in range (repeat):
    word=input()
    real_word=word+word
    if real_word.find(what)!=-1:
        howmany+=1
print(howmany)