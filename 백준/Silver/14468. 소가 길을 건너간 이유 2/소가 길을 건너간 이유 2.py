word=input()
answer=0
for i in range(52):
    for j in range(i+1, 52):
        if word[i]==word[j]:
            l=word[i:j+1]
            for k in l:
                if l.count(k)==1:
                    answer+=1
print(answer//2)