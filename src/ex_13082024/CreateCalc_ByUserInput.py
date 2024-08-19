# WAP to take user input and perform Sum , Subtraction, Multiplication & Division
# Create a Calc

"""num1 = input("Enter you num 1")
num2 = input("Enter you num 2")

print(type(num1))
print(type(num2))

print("Sum is" , num1+num2)
print("sub is" , num1-num2)
print("mul" , num1*num2)
print("div is" , num1/num2)"""

# Above code will give error bcz its taking num1 and num2 as a Str as single or double quotes in python is a Str
# Hence we need to explicitly tell here

num1 = int(input("Enter your num1"))
num2 = int(input("Enter your num2"))


print(type(num1))
print(type(num2))

print("Sum is" , num1+num2)
print("sub is" , num1-num2)
print("mul" , num1*num2)
print("div is" , num1/num2)

# Also division in python return Float value however in java if its returning something in float
#it changes it to Int. But python knows many times division return a Float value hene it has kept
# division return value in Float
