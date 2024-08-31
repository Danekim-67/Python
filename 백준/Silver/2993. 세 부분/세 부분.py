str=input()
part=[]
for i in range(len(str)-2):
    for j in range(i+1,len(str)-1):
        for k in range(j+1, len(str)):
            new_str=str[:j][::-1]+str[j:k][::-1]+str[k:][::-1]
            part.append(new_str)
print(min(part))