# # Ternary Operator has - if else condition
# How to write one liner if-else condition
# print("I'll goto Goa" if int(input("Enter your age")) > 18 else "can't go stay at home ")

# Other way to write if-else condition
user_age = int(input("Enter user age"))
if user_age>=18:
    print("I'll goto Goa")
else:
    print("can't go stay at home")

# difference of operator in if condition

# This line wud throw error bcz in if we put condition here we've assigned the value with = operator
# for condition we shud hv a used == if a=10.
a=9
if a==10:
    print("Hello world")
else:
    print("Bye-Bye")

