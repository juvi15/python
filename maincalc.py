from fun import *

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1, "+", num2, "=", add(num1, num2))


print(num1, "-", num2, "=", subtract(num1, num2))

