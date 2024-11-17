n=int(input())
alphabet=["a", "b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
countl=[0]*26
wordl=[]
for i in range(n):
    word1, word2=input().split()
    for j in range(26):
        countl[j]+=max(word1.count(alphabet[j]), word2.count(alphabet[j]))
for i in range(26):
    print(countl[i])
