# WAP that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

num1 = int(input("Enter the 1st num"))
num2 = int(input("Enter the 2nd num"))

if num1 > num2:
    print("Num1 is greater",num1)
if num2 > num1:
    print("Num2 is greater",num2)
else:
    print("Num1 is equal to Num2")
