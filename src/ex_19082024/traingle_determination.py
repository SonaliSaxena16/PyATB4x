"""
WAP that classifies a triangle based on its side lengths.
Info - equilateral triangle (all sides are equal) isosceles (two sides equal) scalene (no sides are equal)
Hint - Use an if-else statement to classify the triangle.

Input -> 3 float no's representing the lengths of the sides,

O/P -> STR which determine type of the triangle

Rough logic -
side1 = ask user to input measurement of side1
side2 = ask user to input measurement of side2
side3 = ask user to input measurement of side3
condition -
side1==side2==side3 -> equilateral triangle
side1==side2 or side1==side3 or side2==3 isosceles
else scalene

 """
side1 = float(input("Enter side1"))
side2 = float(input("Enter side2"))
side3 = float(input("Enter side3"))

if side1==side2==side3:
    print(" equilateral triangle")
elif side1==side2 or side1==side3 or side2==3:
    print("isosceles triangle")
else:
    print("scalene")

