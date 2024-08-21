"""
if condition is true:
    print(its True)
elif chk this condition is true:
      print(its True)
elif chk this condition is true:
      print(its True)
elif chk this condition is true:
      print(its True)
else:
      print(print this else part bcz didn't find any1 condition to be true)
"""

num1 = int(input("Enter 1st num"))
num2 = int(input("Enter 2nd num"))
num3 = int(input("Enter 3rd num"))

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Max is", num3)

# or
max_num = max(num1,num2,num3)
print(max_num)