line=input("enter the line:")
count={}
sentence= line.split()
for word in sentence:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
for k,v in count.items():
    print(k,v)
