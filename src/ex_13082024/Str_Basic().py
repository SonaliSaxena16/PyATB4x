# Strings
name = "Pramod"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

"""
name = "This is a big line"
name = name+1 # This line will throw error bcz we are Adding Str with int 1
print(name)
"""


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




