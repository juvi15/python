#program for pyramid
n=int(input("enter the step size:"))
for i in range(1,n+1):
    k=1
    for j in range(1,i+1):
        print(k,end=' ')
        k+=i
    print()
