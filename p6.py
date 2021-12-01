astr=input("enter the string\n")
char=input("enter the character \n")
print("given string:\n",astr)
print("given character:\n",char)
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("number of time character is presnt in string:\n",res)
