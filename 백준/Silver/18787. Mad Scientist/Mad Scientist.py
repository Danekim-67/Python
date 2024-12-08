n=int(input())
cow1=input()
cow2=input()
count=0
check=False
for i in range(len(cow1)):
    if cow1[i]==cow2[i] and check==True:
        check=False
        count+=1
    elif check==True or cow1[i]!=cow2[i]:
        check=True
print(count)

