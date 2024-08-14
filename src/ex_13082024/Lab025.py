# Strings
name = "Pramod"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a = 9
print(type(a))  # It'll return Int
A = "90"
print(type(A)) # It'll return Str bcz of quotes either double or single

"""name = "This is a big line"
name = name+1 # This line will throw error bcz we are Adding Str with int 1
print(name)"""

# Now in order to concatinate either add 1 in dubl/single quotes or pass Str with 1
name = "This is a big line"
name = name+'1' # This line will throw error bcz we are Adding Str with int 1
print(name)

# OR

name = "This is a big line"
name = name+str(1) # This line will throw error bcz we are Adding Str with int 1
print(name)

first_name = "Sonali "
last_name = "Saxena"


fullName = first_name+last_name
print(fullName)

how_many_plane_i_have= None
# Python does nto have NULL rather it has None
print(how_many_plane_i_have)

# We can assign 0 value as well
value = 0
print(value)

# id -> Returns the identity of an Object : Memory location

age = 19
print(id(age))
a=19
print(id(a))
# Both age and a variable have same memory address bcz python allocate very carefully since both have same value

a=20
print(id(a))




