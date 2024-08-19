# Explain the difference between the = operator and the == operator in Python.
# = operator is used for assignment. In order to assign value to a variable and
# == operator is used for comparison. Ex = a=1 b=2 a==b ? And it returns a Bool value.

# What does the ** operator do in Python, and how is it used?
# ** used as power function. If I want to find the 5 to the power of 3. Then it can be used as 5**3

# What does the ^ operator do in Python, and in what context is it commonly used?
# ^ is a Python Bitwise Operators called as XOR. Binary xor a ^ b will return a value with only the
# bits set in a or in b but not both.

num = int(input("Enter the num you want to find square of"))
print(pow(num, 2))
# or
print(num**2)

num = int(input("Enter the num you want to find cube of"))
print(pow(num, 3))
# or
print(num**3)


