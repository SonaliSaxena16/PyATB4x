print("Hello World")
print("Hello\nWorld") # \n is for New Line
print("Hello\tWorld") # \t is for space of a TAB
print("Helloz\bWorld") # \b is for back space. It'll remove 'z'

# dir = 'C:\Sonali\n.txt' # This'll throw error
# print(type(dir)) # dir comes from Str data type. However I want to declare it as a Directory Location
# dir = "C:\Sonali\n.txt" # having dubl quotes wud take .txt to new line
# print(dir)
# Hence we wud be using 'r' is a Raw String
dir = r"C:\Sonali\n.txt"
print(dir) # now we wud be getting whole text in one go as Directory Address

dir2 = r'C:\Sonali\n.txt'
print(dir2) # Now it'll take dir location in single as well as dubl quote with 'r' keyword applied
# This 'r' keyword wud be used i API & Web Automation when we wud be passing File_path

# name = 'Sonali' Saxena' # Writting like this is syntax error. Solution below use \
name = 'SONALI\'SAXENA'
print(name)
name2 = "Sonali'Saxena"
print(name2)





