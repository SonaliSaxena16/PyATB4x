# WAP to calulate thhe area of a circle, formula ; ^r2, r=radius will be user input
# Logic Building -
# Step1 Figure out the input/output
# input -> r -> data type -> float/int
# pie = 3.14
# power = use either pow() or **
import math

# Output -> float/int area then print(area)
# Step2 : Rough logic building

#area = 3.14*pow(r,2)

# Acual logic -

radius = int(input("Enter the radius of circle"))
print(radius)
area = math.pi*pow(radius,2)
# or instead of math.pi library we can use diretly
area2 = 3.14*radius**2
print(f"{area:.2f}")
print(f"{area2:.2f}")

# One liner logic
print(3.14*(float(input("Enter the radius"))**2))
