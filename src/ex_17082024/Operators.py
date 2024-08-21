# Operands are on which Operation is being performed using Operator

age  = +65 # Euals to is the Assignment Operator
print(age)
num = 1+2 # Here 1 & 2 are Operands and + - * / symbols are Operators and having these numbers
# added subtracted multiplied and divide is being Operation performed

# Types of Operator
# 1 Unary - Only one operan is required
# 2 Binary - Two operan is required

how_many_lamborgini_I_have = -1 # Minus sign is a Unary Operator as it is applied to one only.
print(how_many_lamborgini_I_have) # In output minus sig wud be shown but in point 1 default plus
# sign is applied to 65 but wud not be shown even if I explicitly apply like this +65 still it wud not show


# Arithmetic operators
# Plus Minus Multiply Divide Divmod(//, X%Y, X**Y)

print(5//2) # This Divmod(//) return Quotient
print("Sonali ",5%2) # This Divmod(%) return Remainder
print(2**3) # This Divmod(**) gives POWER of 2*2*2

# Comparison Operator == return result in True False

print(2==2)
print(2==1)

# Not Operator -> This is used, when we want to return Bool value
is_Sonali_veryTall = True
print(not is_Sonali_veryTall) # Python supports 'not' keyword
# print(!(is_Sonali_veryTall)) # This throws error, is not supported in Py its in JAVA

# ! Operator -> This is used, when we want are performing operation on int
x = 10
y = 20
result = x!=y
print("Not equal operator" , result)

# is Operator , will be used in LIST so Pramod will teach later

# Logical Operator -> Returns Bool
# > , < , <= , >=
x=10
y=20
print(x>y) # 10>20 False
print(x<y)

a=5
b=5
print(a>=b) #5>=5
print(a<=b)
f = False
t = True

print(f or t) # In or if any1 is True then result wud be true. It shud be both false to get false in result
# or GATE Concept
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1
# 0 0 = 0
print(f and t) # In and if any1 is False then result wud be False. It shud be both true  to get True result
# and GATE Concept
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
# 0 0 = 0

# Ternary Operator
# if condition then do this
   # else do that

# if my age<13 then I can watch reels
    # else I cannpt

my_age = int(input("Enter your age"))
print("I'll goto Goa" if my_age>18 else "can't go stay at home")

# Explain the difference between the = operator and the == operator in Python.
# = operator is used for assignment. In order to assign value to a variable and
# == operator is used for comparison. Ex = a=1 b=2 a==b ? And it returns a Bool value.

# What does the ** operator do in Python, and how is it used?
# ** used as power function. If I want to find the 5 to the power of 3. Then it can be used as 5**3

# What does the ^ operator do in Python, and in what context is it commonly used?
# ^ is a Python Bitwise Operators called as XOR. Binary xor a ^ b will return a value with only the
# bits set in a or in b but not both. If we've X Y and operation performed X^Y. It says whenever both
# inputs are same the result would be false. No matter if input are True-True or False-False Ex -
# X Y   X^Y
# 0 0   0 - 0 is for False & 1 is for True
# 1 1   0
# 0 1   1
# 1 0   1
