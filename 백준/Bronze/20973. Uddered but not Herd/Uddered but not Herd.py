cowphabet=input()
word=input()
count=1
for i in range(len(word)-1):
    if cowphabet.find(word[i])>=cowphabet.find(word[i+1]):
        count += 1
print(count)

