word=input().upper(); wordlist=list(set(word));l=[]
for i in wordlist:
    count=word.count(i)
    l.append(count)
if l.count(max(l))>=2:
    print("?")
else:
    print(wordlist[l.index(max(l))])